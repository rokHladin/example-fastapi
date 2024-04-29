"""
This module handles user-related operations using SQLAlchemy ORM Session for 
database interactions.
"""

from sqlalchemy.orm import Session

from app import models, schemas, utils
from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the database.

    Args:
        user (schemas.UserCreate): The user data to be created.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        models.User: The newly created user object.
    """
    # hash the password
    hashed_password = utils.my_hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    # This returns data, so we can display it
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by their ID.

    Args:
        id (int): The ID of the user to retrieve.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        User: The user object.

    Raises:
        HTTPException: If the user with the specified ID is not found.
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} was not found",
        )
    return user
