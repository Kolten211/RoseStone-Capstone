from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models.db import db
from app.models import User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/<int:user_id>/score')
def update_user_score(user_id):
    data = request.get_json()
    new_score = data.get('score')

    user = User.query.get(user_id)
    if not user:
        return{'message': "User not found"}
    
    user.user_score = new_score
    db.session.commit()

    return {'message': 'Score updates successfully'}