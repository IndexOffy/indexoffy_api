"""empty message

Revision ID: a647b3ca03b7
Revises: 4b4fa91b6679
Create Date: 2021-03-21 22:59:12.803065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a647b3ca03b7'
down_revision = '4b4fa91b6679'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('base_log', sa.Column('api_token', sa.String(length=100), nullable=True))
    op.add_column('base_log', sa.Column('ip_address', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('base_log', 'ip_address')
    op.drop_column('base_log', 'api_token')
    # ### end Alembic commands ###
