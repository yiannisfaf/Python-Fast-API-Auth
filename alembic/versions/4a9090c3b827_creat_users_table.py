"""creat users table

Revision ID: 4a9090c3b827
Revises: 438bf319c486
Create Date: 2022-09-28 07:55:39.054291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a9090c3b827'
down_revision = '438bf319c486'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('verification_code', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'users', ['verification_code'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'verification_code')
    # ### end Alembic commands ###