"""effects table

Revision ID: b608c9bcf0e3
Revises: ea25558f704d
Create Date: 2021-01-12 17:02:20.081855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b608c9bcf0e3'
down_revision = 'ea25558f704d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('effect',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('percent_effected', sa.Integer(), nullable=True),
    sa.Column('no_effected', sa.Integer(), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['drug_id'], ['drug.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_effect_name'), 'effect', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_effect_name'), table_name='effect')
    op.drop_table('effect')
    # ### end Alembic commands ###