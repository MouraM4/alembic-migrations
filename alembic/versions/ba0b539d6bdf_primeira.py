"""primeira

Revision ID: ba0b539d6bdf
Revises: 
Create Date: 2022-09-09 15:19:02.138113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba0b539d6bdf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('pessoa')
