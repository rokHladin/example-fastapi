# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring

import pytest

from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    def validate(post):
        return schemas.PostOut(**post)

    posts_map = map(validate, res.json())
    posts_list = list(posts_map)

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200


def test_unauthorized_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401
    assert res.json() == {"detail": "Not authenticated"}


def test_unauthorized_get_one_posts(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    assert res.json() == {"detail": "Not authenticated"}


def test_get_one_post_not_exist(authorized_client, test_posts):
    test_id = 100
    res = authorized_client.get(f"/posts/{test_id}")
    assert res.status_code == 404
    assert res.json() == {"detail": f"Post with id: {test_id} was not found"}


def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**res.json())
    assert res.status_code == 200
    assert post.Post.title == test_posts[0].title
    assert post.Post.content == test_posts[0].content
    assert post.Post.owner_id == test_posts[0].owner_id
    assert post.Post.id == test_posts[0].id
    assert post.votes == 0


@pytest.mark.parametrize(
    "title, content, published",
    [("New title", "New content", True), ("Another title", "Another content", False)],
)
def test_create_post(
    authorized_client, test_user, test_posts, title, content, published
):
    res = authorized_client.post(
        "/posts/", json={"title": title, "content": content, "published": published}
    )
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user["id"]


def test_create_post_default_published_true(authorized_client, test_user):
    res = authorized_client.post(
        "/posts/", json={"title": "New title", "content": "New content"}
    )
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.published is True
    assert created_post.owner_id == test_user["id"]


def test_unauthorized_create_post(client, test_posts):
    res = client.post("/posts/", json={"title": "New title", "content": "New content"})
    assert res.status_code == 401
    assert res.json() == {"detail": "Not authenticated"}


def test_unauthorized_delete_post(client, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401
    assert res.json() == {"detail": "Not authenticated"}


def test_delete_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204


def test_delete_post_non_exist(authorized_client, test_user, test_posts):
    test_id = 10000
    res = authorized_client.delete(f"/posts/{test_id}")
    assert res.status_code == 404


def test_delete_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403
    assert res.json() == {"detail": "You do not have permission to delete this post"}


def test_update_post(authorized_client, test_user, test_posts):
    res = authorized_client.put(
        f"/posts/{test_posts[0].id}",
        json={
            "title": "Updated title",
            "content": "Updated content",
            "published": False,
        },
    )
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == "Updated title"
    assert updated_post.content == "Updated content"
    assert updated_post.published is False


def test_update_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.put(
        f"/posts/{test_posts[3].id}",
        json={
            "title": "Updated title",
            "content": "Updated content",
            "published": False,
        },
    )
    assert res.status_code == 403
    assert res.json() == {"detail": "You do not have permission to update this post"}


def test_unauthorized_user_update_post(client, test_posts):
    res = client.put(
        f"/posts/{test_posts[0].id}",
        json={
            "title": "Updated title",
            "content": "Updated content",
            "published": False,
        },
    )
    assert res.status_code == 401
    assert res.json() == {"detail": "Not authenticated"}


def test_update_post_not_exist(authorized_client, test_posts):
    test_id = 1000
    res = authorized_client.put(
        f"/posts/{test_id}",
        json={
            "title": "Updated title",
            "content": "Updated content",
            "published": False,
        },
    )
    assert res.status_code == 404
