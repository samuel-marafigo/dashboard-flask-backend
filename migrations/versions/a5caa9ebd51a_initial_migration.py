"""Initial migration

Revision ID: a5caa9ebd51a
Revises: 
Create Date: 2024-07-01 11:06:46.010959

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a5caa9ebd51a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'attendances',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('timestamp', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('unit', sa.String(255), nullable=False),
        sa.Column('quantity', sa.Float, nullable=False)
    )

def downgrade():
    op.drop_table('attendances')
