"""add last few columns to posts table

Revision ID: b1fdf3b59168
Revises: dc1e542fbbaf
Create Date: 2024-04-29 17:26:16.736641

"""

from typing import Sequence, Union
from xmlrpc import server

import sqlalchemy as sa

from alembic import op

# pylint: disable=no-member

# revision identifiers, used by Alembic.
revision: str = "b1fdf3b59168"
down_revision: Union[str, None] = "dc1e542fbbaf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean, nullable=False, server_default="true"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
