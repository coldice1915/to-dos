"""empty message

Revision ID: e6f34092e46a
Revises: 9b78b7ca3992
Create Date: 2019-12-23 16:03:16.770695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6f34092e46a'
down_revision = '9b78b7ca3992'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todolists', 'completed')
    # ### end Alembic commands ###