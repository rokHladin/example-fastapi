import imp

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app import schemas
from app.config import settings
from app.database import Base, get_db
from app.main import app
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