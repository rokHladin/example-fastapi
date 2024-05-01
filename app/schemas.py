"""
This module defines the Pydantic models (schemas) for your application. 
These models are used for data validation, serialization and documentation.
"""

from datetime import datetime

from fastapi.background import P
from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated



# This is a schema, this ensures that the data request/response is valid
class PostBase(BaseModel):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the post.
    """

    title: str
    content: str
    published: bool = True  # Default value if it is not specified


# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# # If we only provide published, user cannot edit any other property other than published
# class UpdatePost(BaseModel):
# 	title: str
# 	content: str
# 	published: bool


# It inherites from PostBase, so it has all the attributes of PostBase
class PostCreate(PostBase):
    """
    Represents a request schema for creating a new post.

    This class inherits from the `PostBase` class
    and does not add any additional attributes or methods.
    """


class UserOut(BaseModel):
    """
    Represents the output schema for a user.
    """

    id: int
    email: EmailStr
    created_at: datetime

    class ConfigDict:
        """
        Configuration class for the schema.

        Attributes:
            orm_mode (bool): Flag indicating whether the schema should be used in ORM mode.
        """

        orm_mode = True


class Post(PostBase):
    """
    Represents a post object with additional properties.

    Attributes:
        id (int): The unique identifier of the post.
        created_at (datetime): The timestamp when the post was created.
        owner_id (int): The ID of the post owner.
        owner (UserOut): The user object representing the owner of the post.
    """

    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class ConfigDict:
        """
        Configuration class for the schema.
        """

        orm_mode = True
        
class PostOut(BaseModel):
    Post: Post
    votes: int


class UserCreate(BaseModel):
    """
    Represents the data required to create a new user.

    Attributes:
        email (EmailStr): The email address of the user.
        password (str): The password of the user.
    """

    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """
    Represents the login credentials of a user.

    Attributes:
        email (EmailStr): The email address of the user.
        password (str): The password of the user.
    """

    email: EmailStr
    password: str


class Token(BaseModel):
    """
    Represents a token object.

    Attributes:
        access_token (str): The access token.
        token_type (str): The type of the token.
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Represents the data contained in a token.

    Attributes:
        id (Optional[str]): The ID associated with the token. Defaults to None.
    """

    id: str | None = None


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]
