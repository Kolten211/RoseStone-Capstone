from .db import db, environment, SCHEMA, add_prefix_for_prod

class Question(db.Model):
    __tablename__ = "questions"

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }

    id = db.Column(db.Integer, primary_key = True)
    question_text = db.Column(db.String(25), nullable = False)
    audio_file = db.Column(db.String)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'))
    
    word = db.relationship('Word')
    answers = db.relationship('Answer', backref=db.backref('questions'))
    lessons = db.relationship('Lesson', secondary='lesson_question', back_populates="questions")