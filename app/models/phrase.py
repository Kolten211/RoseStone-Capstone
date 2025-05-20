from .db import db, environment, SCHEMA

class Phrase(db.Model):
    __tablename__ = 'phrases'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(50), nullable = False) ##, unique = True
    translation = db.Column(db.String(50))
   
    lessons = db.relationship('Lesson', secondary='lessons_phrases', back_populates= 'phrases', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'phrase': self.phrase,
            'translation': self.translation,
        }