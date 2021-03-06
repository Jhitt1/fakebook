"""empty message

Revision ID: b79a8e85d708
Revises: 9908fb29ea32
Create Date: 2022-02-17 13:29:24.764295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b79a8e85d708'
down_revision = '9908fb29ea32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cart', 'quantity')
    # ### end Alembic commands ###
