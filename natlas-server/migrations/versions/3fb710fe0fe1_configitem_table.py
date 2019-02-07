"""ConfigItem table

Revision ID: 3fb710fe0fe1
Revises: c5cf61d816c9
Create Date: 2019-02-05 21:08:03.919504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fb710fe0fe1'
down_revision = 'c5cf61d816c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=256), nullable=True),
    sa.Column('value', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('config_item')
    # ### end Alembic commands ###