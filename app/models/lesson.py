from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Lesson(db.Model):
    __tablename__='lessons'

    if environment == "production":
        __table_args__={'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    difficulty = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    description = db.Column(db.String(255), nullable=False)
    words = relationship('Word', secondary='lessons_words', backref=db.backref('lessons', lazy=True))
    phrases = relationship('Phrase', secondary='lesson_phrases', backref=db.backref('phrases', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'difficulty': self.difficulty,
            'user_id': self.user_id,
            'decription': self.description
        }
    

# from .word import Word
# from .phrase import Phrase
from .user import User