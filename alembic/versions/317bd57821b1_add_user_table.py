"""add user table

Revision ID: 317bd57821b1
Revises: d0e4172dd045
Create Date: 2024-04-29 17:05:15.238257

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# pylint: disable=no-member

# revision identifiers, used by Alembic.
revision: str = "317bd57821b1"
down_revision: Union[str, None] = "d0e4172dd045"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("password", sa.String, nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade() -> None:
    op.drop_table("users")
