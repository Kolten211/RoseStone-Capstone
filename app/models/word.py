from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship
class Word(db.Model):
    __tablename__ = 'words'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(25), nullable = False) ##, unique = True
    translation = db.Column(db.String(255))
    part_of_speech = db.Column(db.String(255))
    audio_url = db.Column(db.String(2048))
    
    lessons = relationship('Lesson', secondary='lessons_words', backref=db.backref('Vocabulary', lazy='dynamic'))

    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'translation': self.translation,
            'part_of_speech': self.part_of_speech,
            'audio_url': self.audio_url
        }