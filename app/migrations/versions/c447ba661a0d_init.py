"""init

Revision ID: c447ba661a0d
Revises: 
Create Date: 2024-11-10 16:10:34.267835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c447ba661a0d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=125), nullable=False),
    sa.Column('email', sa.String(length=125), nullable=False),
    sa.Column('password', sa.String(length=125), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('conversion_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conversion_type', sa.Enum('JSON_TO_EXCEL', 'EXCEL_TO_JSON', name='conversiontypes'), nullable=False),
    sa.Column('file_path', sa.String(length=125), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_conversion_records_id'), 'conversion_records', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_conversion_records_id'), table_name='conversion_records')
    op.drop_table('conversion_records')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
