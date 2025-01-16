"""empty message

Revision ID: d2d46ab9bc62
Revises: 1003a55e912a
Create Date: 2025-01-16 07:43:53.823211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2d46ab9bc62'
down_revision = '1003a55e912a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('phrases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('translation', sa.String(length=50), nullable=True))
        batch_op.drop_column('use_case')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('phrases', schema=None) as batch_op:
        batch_op.add_column(sa.Column('use_case', sa.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('translation')

    # ### end Alembic commands ###
