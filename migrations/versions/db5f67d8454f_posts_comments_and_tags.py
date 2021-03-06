"""posts, comments, and tags

Revision ID: db5f67d8454f
Revises: bde732ac9f71
Create Date: 2021-01-23 11:48:12.283251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db5f67d8454f'
down_revision = 'bde732ac9f71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('body', sa.String(length=6000), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_category'), 'post', ['category'], unique=False)
    op.create_index(op.f('ix_post_title'), 'post', ['title'], unique=False)
    op.create_table('affliction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('condition_id', sa.Integer(), nullable=True),
    sa.Column('condition_name', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['condition_id'], ['condition.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('condition_id', sa.Integer(), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['condition_id'], ['condition.id'], ),
    sa.ForeignKeyConstraint(['drug_id'], ['drug.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    op.drop_table('comment')
    op.drop_table('affliction')
    op.drop_index(op.f('ix_post_title'), table_name='post')
    op.drop_index(op.f('ix_post_category'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
