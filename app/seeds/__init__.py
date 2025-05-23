from flask.cli import AppGroup
from .users import seed_users, undo_users
from .lesson import seed_lessons, undo_lessons
from .demo_user_words import seed_demo_user_words, undo_demo_user_words
# from .word import undo_words
# from .phrase import undo_phrases
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_lessons()
        undo_demo_user_words()
        # undo_words()
        # undo_phrases()
    seed_users()
    seed_lessons()
    seed_demo_user_words()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_lessons()
    undo_demo_user_words()
    # undo_words()
    # undo_phrases()
    # Add other undo functions here
