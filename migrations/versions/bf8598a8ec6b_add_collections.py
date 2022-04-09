"""Add collections

Revision ID: bf8598a8ec6b
Revises: a494bb96bb35
Create Date: 2021-08-13 10:00:44.986425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf8598a8ec6b'
down_revision = 'a494bb96bb35'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collection_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collection_id', sa.Integer(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['collection.id'], ),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('collection_image')
    op.drop_table('collection')
