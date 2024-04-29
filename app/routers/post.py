"""
This module handles operations related to posts, such as creating, retrieving, 
updating, and deleting posts. It uses SQLAlchemy ORM Session for database interactions, 
FastAPI's APIRouter for routing, and Depends for dependency injection.
"""

from typing import Callable

from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models, oath2, schemas
from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException, Response, status

func: Callable

router = APIRouter(prefix="/posts", tags=["Posts"])


# Retreiving data
@router.get("/", response_model=list[schemas.PostOut])
def get_posts(
    db: Session = Depends(get_db),
    current_user=Depends(oath2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: str | None = "",
):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    print(limit)

    posts = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )
    print(posts)
    # Convert results to a list of dictionaries
    # results = [{"post": post, "votes": votes} for post, votes in results]

    return posts


# Response_model is used so we can return only what we want
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# This is how we force users to be logged in before they can post
def create_posts(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(oath2.get_current_user),
):

    print(current_user.email)
    # cursor.execute(f"""INSERT INTO posts (title, content, published) VALUES ('{post.title}', '{post.content}', {post.published}) RETURNING *;""")
    # This sanatizes the input from sql injection, if we used f-strings, we would be vulnerable to sql injection
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
    #             (post.title, post.content, post.published))
    # new_post = cursor.fetchone()

    # # This is how you commit changes to the database
    # conn.commit()
    # new_post = models.Post(title = post.title, content = post.content, published = post.published)

    # This unpacks dictionary of post and maps it to a post model
    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    # This returns data, so we can display it
    db.refresh(new_post)
    return new_post


@router.get("/{post_id}", response_model=schemas.PostOut)
# It validates that id is int
def get_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oath2.get_current_user),
):

    # cursor.execute("""SELECT * FROM posts WHERE id = %s;""", (str(id),))
    # # A little more efficient than fetchall
    # post = cursor.fetchone()

    posts = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id).filter(models.Post.id == post_id).first()
    )  # Faster than .all(), because it does not look further

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {post_id} was not found",
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: {id} was not found"}

    # if posts.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #         detail = "You do not have permission to get this post")
    return posts


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oath2.get_current_user),
):
    """
    Delete a post from the database.

    Args:
        post_id (int): The ID of the post to be deleted.
        db (Session, optional): The database session. Defaults to Depends(get_db).
        current_user (User, optional): The current authenticated user.
        Defaults to Depends(oath2.get_current_user).

    Returns:
        Response: A response with status code 204 (No Content) if the post is successfully deleted.

    Raises:
        HTTPException: If the post with the specified ID does not exist or
        the current user does not have permission to delete the post.
    """
    # deleting post
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *;""", (str(id),))
    # deleted_post = cursor.fetchone()
    # # We need to commit changes to the database
    # conn.commit()

    query = db.query(models.Post).filter(
        models.Post.id == post_id
    )  # You can also use get(), to serach for primary key
    post = query.first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot delete post, because post with id: {post_id} does not exist",
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to delete this post",
        )

    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{post_id}", response_model=schemas.Post)
def update_post(
    post_id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(oath2.get_current_user),
):
    """
    Update a post with the given post_id.

    Args:
        post_id (int): The ID of the post to update.
        updated_post (schemas.PostCreate): The updated post data.
        db (Session, optional): The database session. Defaults to Depends(get_db).
        current_user (User, optional): The current authenticated user.
        Defaults to Depends(oath2.get_current_user).

    Returns:
        models.Post: The updated post.

    Raises:
        HTTPException: If the post with the given post_id does not exist or
        the current user does not have permission to update the post.
    """
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot update post, because post with id: {post_id} does not exist",
        )

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to update this post",
        )

    post_query.update(
        {
            models.Post.title: updated_post.title,
            models.Post.content: updated_post.content,
            models.Post.published: updated_post.published,
        },
        synchronize_session=False,
    )
    db.commit()

    return post_query.first()
