"""add user

Revision ID: b3e5f9b6f0dd
Revises: c1bf62f8f88d
Create Date: 2021-01-13 19:23:11.434146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3e5f9b6f0dd'
down_revision = 'c1bf62f8f88d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('update_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('login', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARBINARY(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.add_column('employees', sa.Column('user_id', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employees', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
