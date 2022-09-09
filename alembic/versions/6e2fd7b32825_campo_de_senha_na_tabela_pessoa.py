"""campo de senha na tabela pessoa

Revision ID: 6e2fd7b32825
Revises: ba0b539d6bdf
Create Date: 2022-09-09 15:36:52.694187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e2fd7b32825'
down_revision = 'ba0b539d6bdf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pessoa', sa.Column('senha', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pessoa', 'senha')
    # ### end Alembic commands ###
