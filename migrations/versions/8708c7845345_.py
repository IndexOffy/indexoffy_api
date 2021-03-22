"""empty message

Revision ID: 8708c7845345
Revises: a647b3ca03b7
Create Date: 2021-03-21 23:58:27.827790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8708c7845345'
down_revision = 'a647b3ca03b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('base_log', sa.Column('function', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('base_log', 'function')
    # ### end Alembic commands ###
