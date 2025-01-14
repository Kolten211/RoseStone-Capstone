from .db import db, environment, SCHEMA, add_prefix_for_prod
from app.models import Word, Lesson

class LessonWord(db.Model):
    __tablename__ = 'lessons_words'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }
    
    lesson_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('lessons.id')), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('words.id')), nullable=False)
    