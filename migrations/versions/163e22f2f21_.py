"""Create origin table and link to winery

Revision ID: 163e22f2f21
Revises: be1615a3ac
Create Date: 2019-04-07 12:37:30.552861

"""

# revision identifiers, used by Alembic.
revision = '163e22f2f21'
down_revision = 'be1615a3ac'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('origin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('region', sa.String(length=256), nullable=False),
    sa.Column('country', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('winery', sa.Column('origin_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'winery', 'origin', ['origin_id'], ['id'])


def downgrade():
    op.drop_constraint(None, 'winery', type_='foreignkey')
    op.drop_column('winery', 'origin_id')
    op.drop_table('origin')
