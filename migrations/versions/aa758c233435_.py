"""empty message

Revision ID: aa758c233435
Revises: 28dcc0d2933d
Create Date: 2024-09-20 17:05:58.971478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa758c233435'
down_revision: Union[str, None] = '28dcc0d2933d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
