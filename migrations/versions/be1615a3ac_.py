"""create winery table

Revision ID: be1615a3ac
Revises: 4f2e2c180af
Create Date: 2019-04-07 10:41:37.630828

"""

# revision identifiers, used by Alembic.
revision = 'be1615a3ac'
down_revision = '4f2e2c180af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('winery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('winery')
