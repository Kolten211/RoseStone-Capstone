from .db import db
from sqlalchemy.orm import relationship

class LearnedPhrase(db.Model):
    __tablename__ = 'learned_phrases'


    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    phrase_id = db.Column(db.Integer, db.ForeignKey('phrases.id'), nullable=False)
    date_learned = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = relationship('User', backref='learned_phrases')

    phrase = relationship('Phrase', backref='learned_by')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'phrase_id': self.phrase_id,
            'date_learned': self.date_learned,
            'phrase': self.phrase.to_dict() if self.phrase else None,  # Include phrase details if available
        }
    

from .phrase import Phrase
from .user import User