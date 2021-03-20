"""empty message

Revision ID: ecb6aed96a17
Revises: 004f3ec2f687
Create Date: 2021-03-20 20:36:29.647005

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ecb6aed96a17'
down_revision = '004f3ec2f687'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('api_token', table_name='api_token')
    op.drop_table('api_token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_token',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.Column('date_modified', mysql.DATETIME(), nullable=True),
    sa.Column('base_customer', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=False),
    sa.Column('api_token', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=256), nullable=False),
    sa.Column('api_type', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=False),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('`status` in (0,1)', name='CONSTRAINT_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('api_token', 'api_token', ['api_token'], unique=True)
    # ### end Alembic commands ###
