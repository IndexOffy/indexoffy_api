"""empty message

Revision ID: 24152e2f4bfd
Revises: 3dfeb687c12f
Create Date: 2021-03-20 17:26:39.851603

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '24152e2f4bfd'
down_revision = '3dfeb687c12f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_user', sa.Column('score', sa.String(length=256), nullable=False))
    op.drop_column('api_user', 'level')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_user', sa.Column('level', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=256), nullable=False))
    op.drop_column('api_user', 'score')
    # ### end Alembic commands ###