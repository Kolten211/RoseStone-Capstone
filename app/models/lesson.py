from .db import db, environment, SCHEMA, add_prefix_for_prod

class Lesson(db.Model):
    __tablename__='lessons'

    if environment == "production":
        __table_args__={'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    word_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('words.id')), nullable=False)
    phrase_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('phrases.id')))
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('user.id')))
    description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'word_id': self.word_id,
            'phrase_id': self.phrase_id,
            'decription': self.description
        }
    

from .word import Word
from .phrase import Phrase
from .user import User