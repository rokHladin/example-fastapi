"""
This module handles the creation and verification of JWT tokens for user authentication. 
It uses the jose library for JWT operations, SQLAlchemy ORM Session for database interactions, 
and FastAPI's Depends and HTTPException for dependency injection and exception handling.
"""

from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app import database, models, schemas
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# SECRET_KEY
# Algorith
# Expiration time

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict) -> str:
    """
    Create an access token with the provided data.

    Args:
        data (dict): The data to be encoded in the access token.

    Returns:
        str: The encoded access token.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def verify_access_token(token: str, credentals_exception) -> schemas.TokenData:
    """
    Verify the access token and return the token data.

    Args:
        token (str): The access token to verify.
        credentals_exception: The exception to raise if the token is invalid.

    Returns:
        TokenData: The token data extracted from the access token.

    Raises:
        credentals_exception: If the access token is invalid or does not contain a user ID.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("user_id")

        if user_id is None:
            raise credentals_exception
        token_data = schemas.TokenData(id=str(user_id))
    except JWTError as exc:
        raise credentals_exception from exc
    return token_data


# Get the token from the request and extract the user_id
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)
) -> models.User:
    """
    Retrieves the current user based on the provided access token.

    Args:
        token (str): The access token used for authentication.
        db (Session): The database session.

    Returns:
        User: The user associated with the access token.

    Raises:
        HTTPException: If the credentials cannot be validated.
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    verified_token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == verified_token.id).first()
    return user
