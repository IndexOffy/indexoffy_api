"""empty message

Revision ID: 1b9a259efb2a
Revises: f7d3a34be13b
Create Date: 2021-04-04 20:13:36.725286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b9a259efb2a'
down_revision = 'f7d3a34be13b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('base_token_ibfk_1_idx_idx', 'base_token', ['base_customer'], unique=False)
    # ### end Alembic commands ###