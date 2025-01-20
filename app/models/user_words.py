from .db import db
from sqlalchemy.orm import relationship

class LearnedWord(db.Model):
    __tablename__ = 'learned_words'


    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    date_learned = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = relationship('User', backref='learned_words')

    word = relationship('Word', backref='learned_by')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'word_id': self.word_id,
            'date_learned': self.date_learned,
            'word': self.word.to_dict() if self.word else None,  # Include word details if available
        }
    

from .word import Word
from .user import User