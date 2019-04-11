"""Create appellation table

Revision ID: 15e62d4d1df
Revises: 163e22f2f21
Create Date: 2019-04-07 13:02:43.543601

"""

# revision identifiers, used by Alembic.
revision = '15e62d4d1df'
down_revision = '163e22f2f21'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('appellation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('origin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['origin_id'], ['origin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('appellation')
