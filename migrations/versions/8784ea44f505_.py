"""empty message

Revision ID: 8784ea44f505
Revises: e8630d6603be
Create Date: 2021-10-09 19:24:23.726891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8784ea44f505'
down_revision = 'e8630d6603be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transaction_type', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('transaction_type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('types')
    # ### end Alembic commands ###