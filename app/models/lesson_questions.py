from .db import db, environment, SCHEMA, add_prefix_for_prod

class LessonQuestion(db.Model):
    __table_name__ = ' lesson_question'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    lesson_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('lessons.id')), primary_key=True, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('questions.id')), primary_key=True, nullable=False)