from .db import db, environment, SCHEMA, add_prefix_for_prod

class LessonWord(db.Model):
    __tablename__ = 'lessons_words'

    if environment == "production":
        __table_args__ = { 'schema': SCHEMA }
    
    lesson_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('lessons.id')), primary_key=True, nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('words.id')), primary_key=True, nullable=False)
    # lesson = relationship("Lesson", backref="words")
    # word = relationship("Word", backref="lessons")