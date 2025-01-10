from .db import db, environment, SCHEMA


class Phrase(db.Model):
    __tablename__ = 'phrases'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    phrase = db.Column(db.String(50), nullable = False, unique = True)
    use_case = db.Column(db.String(50))
    learned = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'phrase': self.word,
            'use_case': self.use_case,
            'learned': self.learned
        }