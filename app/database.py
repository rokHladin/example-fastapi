"""
This module sets up the database connection using SQLAlchemy. It includes the 
creation of the SQLAlchemy engine, session and base class for declarative models.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.database_username}:"
    f"{settings.database_password}@{settings.database_hostname}:"
    f"{settings.database_port}/{settings.database_name}"
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    """
    Returns a database session.

    Yields:
        SessionLocal: The database session.

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# If you want to directly connect to database without using SQLAlchemy
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = config.DB_USER,
#                             password = config.DB_PASSWORD, cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was successful')
#         break

#     except Exception as error:
#         print("Connection to database failed")
#         print(f"The error was: {error}")
#         time.sleep(2)
