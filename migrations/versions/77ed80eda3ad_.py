"""empty message

Revision ID: 77ed80eda3ad
Revises: 4b730f360bc1
Create Date: 2021-04-03 05:26:03.039673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77ed80eda3ad'
down_revision = '4b730f360bc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'base_token', 'base_customer', ['base_customer'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'base_token', type_='foreignkey')
    # ### end Alembic commands ###