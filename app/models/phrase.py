from .db import db, environment, SCHEMA
from sqlalchemy.orm import relationship

class Phrase(db.Model):
    __tablename__ = 'phrases'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(50), nullable = False) ##, unique = True
    translation = db.Column(db.String(50))
   
    lessons = relationship('Lesson', secondary='lessons_phrases', backref=db.backref('Sentences', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'phrase': self.phrase,
            'translation': self.translation,
        }