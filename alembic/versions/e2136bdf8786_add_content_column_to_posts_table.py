"""add content column to posts table

Revision ID: e2136bdf8786
Revises: ec66c751e6db
Create Date: 2022-07-21 21:59:39.318221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2136bdf8786'
down_revision = 'ec66c751e6db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
