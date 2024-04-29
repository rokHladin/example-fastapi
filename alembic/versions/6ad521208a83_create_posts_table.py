"""Create posts table

Revision ID: 6ad521208a83
Revises: 
Create Date: 2024-04-29 16:38:02.189421

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6ad521208a83"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# pylint: disable=no-member

# Runs the commands for making the changes to the database
def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
    )


# If you mess up, this will undo the changes
def downgrade() -> None:
    op.drop_table("posts")
