"""alteracao no campo email para 100 chars

Revision ID: a9b5e897310f
Revises: dcf1965a3e14
Create Date: 2022-09-09 16:07:26.507157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9b5e897310f'
down_revision = 'dcf1965a3e14'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pessoa', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###
