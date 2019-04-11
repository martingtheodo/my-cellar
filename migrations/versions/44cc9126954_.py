"""Create grape_variety, cuvee and bottle tables

Revision ID: 44cc9126954
Revises: 15e62d4d1df
Create Date: 2019-04-07 13:28:03.915725

"""

# revision identifiers, used by Alembic.
revision = '44cc9126954'
down_revision = '15e62d4d1df'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('grape_variety',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cuvee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('colour', sa.String(length=128), nullable=False),
    sa.Column('winery_id', sa.Integer(), nullable=False),
    sa.Column('appellation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['appellation_id'], ['appellation.id'], ),
    sa.ForeignKeyConstraint(['winery_id'], ['winery.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bottle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vintage', sa.String(length=4), nullable=False),
    sa.Column('cuvee_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=32), nullable=False),
    sa.ForeignKeyConstraint(['cuvee_id'], ['cuvee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cuvee_grape_variety',
    sa.Column('cuvee_id', sa.Integer(), nullable=True),
    sa.Column('grape_variety_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cuvee_id'], ['cuvee.id'], ),
    sa.ForeignKeyConstraint(['grape_variety_id'], ['grape_variety.id'], )
    )


def downgrade():
    op.drop_table('cuvee_grape_variety')
    op.drop_table('bottle')
    op.drop_table('cuvee')
    op.drop_table('grape_variety')
