from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Lesson, Word, Phrase

lesson_routes =  Blueprint('lesson', __name__)

@lesson_routes.route('/')
@login_required
def lessons():
    """
    Query Lessons that a user can add
    """
    current_user

    lessons = Lesson.query.all()

    return {"lessons": [lesson.to_dict for lesson in lessons]}

@lesson_routes.route('/create', methods=['POST'])
@login_required
def create_lesson():
    """
    Create a lesson with learned words and/or phrases
    """

    lesson_data = request.get_json()
    
    if not lesson_data:
        return {"message": "Invalid request body"}, 400
    
    word_ids = lesson_data.get('word_ids', [])

    phrase_ids = lesson_data.get('phrase_ids', [])

    new_lesson = Lesson(**lesson_data)

    for word_id  in word_ids:
        word = Word.query.get(word_id)
        if word:
            new_lesson.words.append(word)

    for phrase_id in phrase_ids:
        phrase = Phrase.query.get(phrase_id)
        if phrase:
            new_lesson.phrases.append(phrase)

    db.session.add(new_lesson)
    db.session.commit()
    
    return new_lesson.to_dict(), 201

@lesson_routes.route('/<int:lesson_id>')
@login_required
def update_lesson(lesson_id):
    """
    Update the description of a lesson
    """

    data = request.json
    lesson = Lesson.query.get(lesson_id)

    if not lesson:
        return {'message': 'Lesson not found'}, 400
    
    if 'description' in data:
        lesson.lesson = data['description']

    db.session.commit()

    return lesson.to_dict()

@lesson_routes.route('/<int:lesson_id>', methods=['DELETE'])
@login_required
def delete_lesson(lesson_id):
    """
    Delete a lesson from learned lessons
    """

    lesson = Lesson.query.get(lesson_id)

    if not lesson:
        return {'message': 'Lesson not found'}, 404
    
    db.session.delete(lesson)
    db.session.commit()

    return {'message': 'Lesson deleted successfully'}