"""added genres table

Revision ID: 428053b48a99
Revises: 4f6dff63f3a8
Create Date: 2024-04-01 14:19:05.705134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '428053b48a99'
down_revision: Union[str, None] = '4f6dff63f3a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
