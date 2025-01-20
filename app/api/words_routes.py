from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Word, LearnedWord

word_routes = Blueprint('words', __name__)


@word_routes.route('/')
@login_required
def words():
    """
    Query all learned/added words a user
    """

    words = Word.query.all() 

    return {'words': [word.to_dict() for word in words]}

@word_routes.route('/create', methods=['POST'])
@login_required
def create_word():
    """
    Create a new word
    """
    word_data = request.get_json()

    if not word_data:
        return {"message": "Invalid request body"}, 400
    
    existing_word = Word.query.filter_by(word=word_data).first()

    if existing_word:
        return {"message": "Word already exists"}, 409
    
    new_word = Word(**word_data)
    # db.session.add(new_word)
    # db.session.commit()

    new_learned_word = LearnedWord(user_id=current_user.id, word_id=new_word)
    db.session.add(new_learned_word)
    db.session.commit()
    
    return new_word.to_dict(), 201

@word_routes.route('/<int:word_id>', methods=['PUT'])
@login_required
def update_word(word_id):
    """
    User update spelling to word to make more sense to them
    """

    data = request.json
    word = LearnedWord.query.filter_by(user_id = current_user.id, word_id = word_id).first()


    if not word:
        return {'message': 'Word not found'}, 404
    
    if 'word' in data:
        word.word = data['word']
    
    db.session.commit()

    return word.to_dict()

@word_routes.route('/<int:word_id>', methods=['DELETE'])
@login_required
def delete_word(word_id):
    """
    Delete a word from learned words
    """

    word = LearnedWord.query.filter_by(user_id = current_user.id, word_id = word_id).first()

    if not word:
        return {'message': 'word not found'}, 404
    
    db.session.delete(word)
    db.session.commit()

    return {'message': 'word deleted successfully'}