"""Create stock table

Revision ID: 5651c474da4
Revises: 44cc9126954
Create Date: 2019-04-07 13:58:15.380072

"""

# revision identifiers, used by Alembic.
revision = '5651c474da4'
down_revision = '44cc9126954'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('stock',
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('bottle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bottle_id'], ['bottle.id'], ),
    sa.PrimaryKeyConstraint('bottle_id')
    )


def downgrade():
    op.drop_table('stock')
