"""empty message

Revision ID: cffb8ee43437
Revises: 08f7ee849c1e
Create Date: 2025-01-15 15:37:29.826447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cffb8ee43437'
down_revision = '08f7ee849c1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lessons_phrases',
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('phrase_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ),
    sa.ForeignKeyConstraint(['phrase_id'], ['phrases.id'], ),
    sa.PrimaryKeyConstraint('lesson_id', 'phrase_id')
    )
    op.create_table('lessons_words',
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['words.id'], ),
    sa.PrimaryKeyConstraint('lesson_id', 'word_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lessons_words')
    op.drop_table('lessons_phrases')
    # ### end Alembic commands ###
