"""
Revision ID: 38bcd0b3d32a
Revises: cc8834175553
Create Date: 2025-01-14 22:24:47.316939
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "38bcd0b3d32a"
down_revision: Union[str, None] = "cc8834175553"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tl_outbox",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("tl_outbox")
