"""empty message

Revision ID: a52ef0307a38
Revises: 13df8d260308
Create Date: 2025-01-18 12:04:07.788094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a52ef0307a38'
down_revision = '13df8d260308'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('native_language', sa.String(length=25), nullable=True))
        batch_op.add_column(sa.Column('learning_language', sa.String(length=25), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('learning_language')
        batch_op.drop_column('native_language')

    # ### end Alembic commands ###
