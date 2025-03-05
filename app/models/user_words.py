from .db import db
from sqlalchemy.orm import relationship

class LearnedWord(db.Model):
    __tablename__ = 'learned_words'


    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    translation = db.Column(db.String(255))
    part_of_speech = db.Column(db.String(255))
    audio_url = db.Column(db.String(2048))
    user_word = db.Column(db.String(255))
    date_learned = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = relationship('User', backref='learned_words')

    word = relationship('Word', backref='learned_by')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'word_id': self.word_id,
            'user_word': self.user_word,
            'translation': self.translation,
            'part_of_speech': self.part_of_speech,
            'audio_url': self.audio_url,
            'date_learned': self.date_learned,
            'word': self.word.to_dict() if self.word else None,  # Include word details if available
        }