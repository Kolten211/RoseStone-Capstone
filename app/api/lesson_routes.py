from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models.db import db
from app.models import Lesson

lesson_routes =  Blueprint('lesson', __name__)

@lesson_routes.route('/')
@login_required
def lessons():
    """
    Query Lessons that a user can add
    """

    lessons = Lesson.query.all()

    return 