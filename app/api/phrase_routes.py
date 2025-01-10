from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Phrase

phrase_routes = Blueprint('phrase', __name__)

@phrase_routes.route('/')
@login_required
def words():
    """
    Query all learned/added phrases of a user
    """

    phrases = Phrase.query.filter_by(learned=True).all()
    
    return {'phrases': [phrase.to_dict() for phrase in phrases]}

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
    
    return new_phrase.to_dict(), 201

@phrase_routes.rotue('/<int:phrase_id>', methods=['PUT'])
@login_required
def update_phrase(phrase_id):
    """
    User update phrase the made
    """

    data = request.json
    phrase = Phrase.query.get(phrase_id)

    if not word:
        return {'message': 'Phrase not found'}, 400
    
    if 'use' in data:
        phrase.phrase = data['use']
    
    db.session.commit()

    return phrase.to_dict()

@phrase_routes.route('/<int:phrase_id>', methods=['DELETE'])
@login_required
def delete_phrase(phrase_id):
    """
    Delete a phrase from learned phrases
    """

    phrase = Phrase.query.get(phrase_id)

    if not phrase:
        return {'message': 'Phrase not found'}, 404
    
    db.session.delete(phrase)
    db.session.commit()

    return {'message': 'phrase deleted successfully'}