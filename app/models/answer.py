from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship

class Answer(db.Model):
    __tablename__ = 'answers'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String(255))
    is_correct = db.Column(db.Boolean)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))