from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable = False)
    lesson_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('lessons.id')), nullable = False)
    score = db.Column(db.Integer, nullable = False)
    completion_date = db.Column(db.DateTime, default = datetime.now)

    user = db.relationship("User", back_populates = 'quiz_attempts')
    lesson = db.relationship("Lesson", back_populates = 'quiz_attempts')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'lesson_id': self.lesson_id,
            'score': self.score,
            'completion_date': self.completion_date
        }