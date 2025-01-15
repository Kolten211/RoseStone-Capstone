from .db import db, environment, SCHEMA, add_prefix_for_prod
from app.models import Phrase, Lesson

class LessonPhrase(db.Model):
    __tablename__ = 'lessons_phrases'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    lesson_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('lessons.id')), primary_key=True, nullable=False)
    phrase_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('phrases.id')), primary_key=True, nullable=False)