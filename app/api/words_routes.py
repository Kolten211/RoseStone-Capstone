import os
import uuid
from flask import Blueprint, request
from flask_login import login_required, current_user
from .aws_helper import upload_file_to_s3, remove_file_from_s3
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
    
    new_word = Word(**word_data)
    db.session.add(new_word)
    db.session.commit()

    new_learned_word = LearnedWord(
        user_id=current_user.id,
        word_id=new_word.id
    )
    db.session.add(new_learned_word)
    db.session.commit()
    
    return new_word.to_dict(), 201

@word_routes.route('/<int:word_id>', methods=['PUT'])
@login_required
def update_word(word_id):
    """
    User update spelling to word to make more sense to them
    """

    # data = request.json
    word = LearnedWord.query.filter_by(user_id = current_user.id, word_id = word_id).first()


    if not word:
        return {'message': 'Word not found'}, 404
    
    if 'word' in request.form:
        word.user_word = request.form['word']
    if 'translation' in request.form:
        word.translation = request.form['translation']
    if 'part_of_speech' in request.form:
        word.part_of__speech = request.form['part_of_speech']
    if 'audio' in request.files:
        audio_file = request.files['audio']

        filename = f"word_{word_id}_{uuid.uuid4.hex}.wav"
        audio_file.filename = filename

        upload_result = upload_file_to_s3(audio_file)

        if "url" not in upload_result:
            return { "errors": upload_result["errors"]}

        word.audio_url = upload_result['url']
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


@word_routes.route('/learned')
@login_required
def learned_words():
    """
    Get all Learned Words of a user
    """

    learned_words = LearnedWord.query.filter_by(user_id=current_user.id).all()
    learned_words_dicts = [lw.word.to_dict() for lw in  learned_words if lw.word]

    return {'learned_words': learned_words_dicts}