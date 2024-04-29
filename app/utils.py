"""
This module provides utility functions for password hashing and verification 
using the passlib library's CryptContext.
"""
from passlib.context import CryptContext

# This defines the hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def my_hash(password: str) -> str:
    """
    Hashes the password using the bcrypt algorithm.
    """
    return pwd_context.hash(password)


def verify(plain_password, hashed_password) -> bool:
    """
    Verify if a plain password matches a hashed password.

    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password to compare against.

    Returns:
        bool: True if the plain password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)
