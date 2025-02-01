"""
Revision ID: 0e6a79cb90ca
Revises: 38bcd0b3d32a
Create Date: 2025-02-01 19:29:35.387066
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = '0e6a79cb90ca'
down_revision: Union[str, None] = '38bcd0b3d32a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('product', 'characteristics')


def downgrade() -> None:
    op.add_column(
        'product',
        sa.Column('characteristics', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    )
