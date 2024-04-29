"""add foreign key to posts table

Revision ID: dc1e542fbbaf
Revises: 317bd57821b1
Create Date: 2024-04-29 17:13:58.799093

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# pylint: disable=no-member

# revision identifiers, used by Alembic.
revision: str = "dc1e542fbbaf"
down_revision: Union[str, None] = "317bd57821b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
