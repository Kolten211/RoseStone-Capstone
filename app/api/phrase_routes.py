from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Phrase, LearnedPhrase

phrase_routes = Blueprint('phrase', __name__)

@phrase_routes.route('/')
@login_required
def phrases():
    """
    Query all learned/added phrases of a user
    """

    phrases = Phrase.query.all()
    
    return {'phrases': [phrase.to_dict() for phrase in phrases]}

@phrase_routes.route('/user_phrases')
@login_required
def get_user_phrases():
    user_phrases = current_user.learned_phrases
    return {'phrases': [phrase.phrase.to_dict() for phrase in user_phrases]}

@phrase_routes.route('/create', methods=['POST'])
@login_required
def create_phrase():
    """
    Create a phrase with learned words
    """

    phrase_data = request.get_json()

    if not phrase_data:
        return {"message": "Invalid request body"}, 400
    
    existing_phrase = Phrase.query.filter_by(phrase=phrase_data).first()

    if existing_phrase:
        return {"message": "phrase already exists"}, 409
    
    new_phrase = Phrase(**phrase_data)
    db.session.add(new_phrase)
    db.session.commit()

    new_learned_phrase = LearnedPhrase(user_id=current_user.id, phrase_id=new_phrase)
    db.session.add(new_learned_phrase)
    db.session.commit()
    
    return new_phrase.to_dict(), 201

@phrase_routes.route('/<int:phrase_id>', methods=['PUT'])
@login_required
def update_phrase(phrase_id):
    """
    User update phrase the made
    """

    data = request.json
    phrase = LearnedPhrase.query.filter_by(user_id = current_user.id, phrase_id = phrase_id).first()

    if not phrase:
        return {'message': 'Phrase not found in user\'s list'}, 400
    
    if 'phrase' in data:
        phrase.phrase = data['phrase']
    
    db.session.commit()

    return phrase.to_dict()

@phrase_routes.route('/<int:phrase_id>', methods=['DELETE'])
@login_required
def delete_phrase(phrase_id):
    """
    Delete a phrase from learned phrases
    """

    phrase = LearnedPhrase.query.filter_by(user_id = current_user.id, phrase_id = phrase_id).first()

    if not phrase:
        return {'message': 'Phrase not found'}, 404
    
    db.session.delete(phrase)
    db.session.commit()

    return {'message': 'Phrase deleted successfully'}