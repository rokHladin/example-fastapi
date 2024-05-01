# Here you define fixtures that are used in multiple tests
# Everything down the scope of this file has access to these fixtures

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import models
from app.config import settings
from app.database import Base, get_db
from app.main import app
from app.oath2 import create_access_token
from fastapi.testclient import TestClient

# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgresapicourse@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.database_username}:"
    f"{settings.database_password}@{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}_test"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Now I have access to database session as well as client
@pytest.fixture()
def session():
    # That way if test failes its going to keep the tables (flag -x)
    # You can use alembic instead
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    # run our code before we run our test
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app=app)
    # run our code after our test finishes


@pytest.fixture()
def test_user(client):
    user_data = {"email": "hello123@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture()
def test_user2(client):
    user_data = {"email": "hello1234@gmail.com", "password": "password123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture()
def token(test_user):
    return create_access_token(data={"user_id": test_user["id"]})


@pytest.fixture()
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}
    return client


@pytest.fixture()
def test_posts(test_user, session, test_user2):
    posts_data = [
        {"title": "Post 1", "content": "Content 1", "owner_id": test_user["id"]},
        {"title": "Post 2", "content": "Content 2", "owner_id": test_user["id"]},
        {"title": "Post 3", "content": "Content 3", "owner_id": test_user["id"]},
        {"title": "Post 4", "content": "Content 4", "owner_id": test_user2["id"]},
    ]

    def create_post_model(post_data):
        return models.Post(**post_data)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()
    session.query(models.Post).all()
    return posts
