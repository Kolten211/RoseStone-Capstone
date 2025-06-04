from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Lesson, Word, Phrase, LearnedWord, LearnedPhrase, User

lesson_routes =  Blueprint('lesson', __name__)

@lesson_routes.route('/')
@login_required
def lessons():
    """
    Query Lessons that a user can add
    """
    current_user

    lessons = Lesson.query.all()

    return {"lessons": [lesson.to_dict() for lesson in lessons]}

@lesson_routes.route('/<int:lesson_id>')
@login_required
def lesson_details(lesson_id):
    """
    To get a specific lesson
    """

    lesson = Lesson.query.get(lesson_id)

    if not lesson:
        return {'message': 'Lesson not found'}, 404
    
    words = lesson.words
    phrases = lesson.phrases

    return {
        'title': lesson.title,
        'difficulty': lesson.difficulty,
        'user_id': lesson.user_id,
        'description': lesson.description,
        'words': [word.to_dict() for word in words],
        'phrases': [phrase.to_dict() for phrase in phrases]
        }

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

    questions = lesson_data.get('questions', [])

    new_lesson = Lesson(**lesson_data)
    new_lesson.questions = questions

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

@lesson_routes.route('/<int:lesson_id>', methods=['PUT'])
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



@lesson_routes.route('/<int:lesson_id>/complete', methods=['POST'])
@login_required
def lesson_complete(lesson_id):
    """
    To add words or phrases when a user completes a lesson 
    """

    lesson = Lesson.query.get(lesson_id)
    user_answers = request.get_json()

    if not user_answers:
        return {'message': "No answers provided"}
    
    total_questions = len(lesson.questions)
    correct_count = 0

    lesson_questions = {q.id: {a.id for a in q.answers if a.is_correct} for q in lesson.questions}

    for question_id_str, submitted_answer_id_str in user_answers.items():
        try: 
            question_id = int(question_id_str)
            submitted_answer_id = int(submitted_answer_id_str)
        except ValueError:
            return {'error': f"Invalid ID format for question or answer: {question_id_str}, {submitted_answer_id_str}"}
        if question_id not in lesson_questions:
            return {'error': f"Question ID {question_id} not part of lesson {lesson_id}"}
        
        correct_answer_ids = lesson_questions[question_id]

        if submitted_answer_id in correct_answer_ids:
            correct_count += 1

    score_percent = (correct_count / total_questions) * 100 if total_questions > 0 else 0

    
    if not lesson:
        return {'message': "No lesson found"}
    
    if lesson.level == 'beginner':
        lesson_words = lesson.words
        for word in lesson_words:
            learned_word = LearnedWord(user_id=current_user.id, word_id=word.id)
            db.session.add(learned_word)

    elif lesson.level == 'intermediate':
        lesson_phrase = lesson.phrases
        for phrase in lesson_phrase:
            learned_phrase = LearnedPhrase(user_id=current_user.id, phrase_id=phrase.id)
            db.session.add(learned_phrase)
    
    elif lesson.level == 'Advanced':
        pass

    db.session.commit()
    return {'message': 'Lesson Completed!'}