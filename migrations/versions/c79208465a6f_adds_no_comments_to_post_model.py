"""adds no_comments to post model

Revision ID: c79208465a6f
Revises: 785dc5ce2e8c
Create Date: 2021-01-25 07:21:41.238424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c79208465a6f'
down_revision = '785dc5ce2e8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('no_comments', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('no_comments')

    # ### end Alembic commands ###