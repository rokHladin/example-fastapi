"""
This module handles authentication-related operations such as login and token 
generation. It uses SQLAlchemy ORM Session for database interactions, FastAPI's 
APIRouter for routing, and OAuth2 for authentication.
"""
from sqlalchemy.orm import Session
from app import database, models, oath2, schemas, utils
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

# OAuth2PasswordRequestFrom returns a username and password
@router.post("/login", response_model=schemas.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    """
    Authenticates the user with the provided credentials and returns an access token.

    Args:
        user_credentials (OAuth2PasswordRequestForm): The user's credentials.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the access token and token type.

    Raises:
        HTTPException: If the credentials are invalid.
    """
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials"
        )

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials"
        )

    # Create a token
    access_token = oath2.create_access_token(data={"user_id": user.id})

    # return token
    return {"access_token": access_token, "token_type": "bearer"}
