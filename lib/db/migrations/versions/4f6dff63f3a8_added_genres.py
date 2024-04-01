"""Added genres

Revision ID: 4f6dff63f3a8
Revises: aa7b8c86331e
Create Date: 2024-04-01 12:43:42.238738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f6dff63f3a8'
down_revision: Union[str, None] = 'aa7b8c86331e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
