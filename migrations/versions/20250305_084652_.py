"""empty message

Revision ID: 00c8700dc6b5
Revises: 87f6eacfd40f
Create Date: 2025-03-05 08:46:52.355045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c8700dc6b5'
down_revision = '87f6eacfd40f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('learned_words', schema=None) as batch_op:
        batch_op.add_column(sa.Column('translation', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('part_of_speech', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('audio_url', sa.String(length=2048), nullable=True))
        batch_op.add_column(sa.Column('user_word', sa.String(length=255), nullable=True))

    with op.batch_alter_table('words', schema=None) as batch_op:
        batch_op.alter_column('translation',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=255),
               existing_nullable=True)
        batch_op.alter_column('part_of_speech',
               existing_type=sa.VARCHAR(length=25),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('words', schema=None) as batch_op:
        batch_op.alter_column('part_of_speech',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=25),
               existing_nullable=True)
        batch_op.alter_column('translation',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=25),
               existing_nullable=True)

    with op.batch_alter_table('learned_words', schema=None) as batch_op:
        batch_op.drop_column('user_word')
        batch_op.drop_column('audio_url')
        batch_op.drop_column('part_of_speech')
        batch_op.drop_column('translation')

    # ### end Alembic commands ###
