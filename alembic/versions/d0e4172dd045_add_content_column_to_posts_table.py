"""Add content column to posts table

Revision ID: d0e4172dd045
Revises: 6ad521208a83
Create Date: 2024-04-29 16:54:36.403500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# pylint: disable=no-member
# revision identifiers, used by Alembic.
revision: str = 'd0e4172dd045'
down_revision: Union[str, None] = '6ad521208a83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
