"""empty message

Revision ID: 46b1fd6e58cf
Revises: 4e1851f54be5
Create Date: 2024-09-21 12:12:19.613616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46b1fd6e58cf'
down_revision: Union[str, None] = '4e1851f54be5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bets', 'start_date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.alter_column('bets', 'end_date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.alter_column('cars', 'year',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.drop_constraint('cars_category_key', 'cars', type_='unique')
    op.drop_constraint('cars_marka_key', 'cars', type_='unique')
    op.drop_constraint('cars_model_key', 'cars', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('cars_model_key', 'cars', ['model'])
    op.create_unique_constraint('cars_marka_key', 'cars', ['marka'])
    op.create_unique_constraint('cars_category_key', 'cars', ['category'])
    op.alter_column('cars', 'year',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)
    op.alter_column('bets', 'end_date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)
    op.alter_column('bets', 'start_date',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###
