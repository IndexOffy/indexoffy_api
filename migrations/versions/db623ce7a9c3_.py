"""empty message

Revision ID: db623ce7a9c3
Revises: 739a3343e8b7
Create Date: 2021-03-19 23:02:31.259883

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'db623ce7a9c3'
down_revision = '739a3343e8b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=192), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('api_token', sa.Column('api_token', sa.String(length=256), nullable=False))
    op.drop_index('apit_token', table_name='api_token')
    op.create_unique_constraint(None, 'api_token', ['api_token'])
    op.drop_column('api_token', 'apit_token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_token', sa.Column('apit_token', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=False))
    op.drop_constraint(None, 'api_token', type_='unique')
    op.create_index('apit_token', 'api_token', ['apit_token'], unique=True)
    op.drop_column('api_token', 'api_token')
    op.drop_table('base_customer')
    # ### end Alembic commands ###
