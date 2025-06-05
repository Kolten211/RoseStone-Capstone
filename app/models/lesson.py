from .db import db, environment, SCHEMA, add_prefix_for_prod


class Lesson(db.Model):
    __tablename__='lessons'

    if environment == "production":
        __table_args__={'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    difficulty = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    description = db.Column(db.String(255), nullable=False)
    # questions = db.Column(db.String, nullable=True)
    # answers = db.Column(db.String, nullable=True)

    questions = db.relationship('Question', secondary='lesson_question', back_populates="lessons")
    words = db.relationship('Word', secondary='lessons_words', back_populates= "lessons", lazy='dynamic')
    phrases = db.relationship('Phrase', secondary='lessons_phrases', back_populates= "lessons", lazy='dynamic')
    quiz_attempts = db.relationship('QuizAttempt', back_populates = 'lesson', cascade = 'all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'difficulty': self.difficulty,
            'user_id': self.user_id,
            'decription': self.description,
            "questions": self.questions
        }
    

