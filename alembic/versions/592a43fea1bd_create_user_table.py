"""Create user table

Revision ID: 592a43fea1bd
Revises: 
Create Date: 2023-10-25 17:32:12.198122

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '592a43fea1bd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('user_name', sa.Text(), nullable=True),
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('second_name', sa.Text(), nullable=True),
    sa.Column('is_premium', sa.Boolean(), nullable=False),
    sa.Column('role', sa.Enum('USER', 'ADMINISTRATOR', name='role'), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('user_id', name=op.f('uq_user_user_id'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###