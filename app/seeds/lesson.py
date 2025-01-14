from app.models import db, Lesson, environment, SCHEMA
from sqlalchemy.sql import text

starter_lessons = [
    {
        'title': 'Me, Myself, and I',
        'words': [
            {'word': 'I', 'part_of_speech': 'pronoun'},
            {'word': 'me', 'part_of_speech': 'pronoun'},
            {'word': 'you', 'part_of_speech': 'pronoun'},
            {'word': 'he', 'part_of_speech': 'pronoun'},
            {'word': 'she', 'part_of_speech': 'pronoun'},
        ],
        'phrases': [
            "Hello, my name is...",
            "How are you?",
            "I am fine, thank you.",
        ]
    },
    {
        'lesson_title': 'Greetings',
        'words': [
            {'word': 'hello', 'part_of_speech': 'interjection'},
            {'word': 'hi', 'part_of_speech': 'interjection'},
            {'word': 'good', 'part_of_speech': 'adjective'}, 
            {'word': 'morning', 'part_of_speech': 'noun'},
            {'word': 'afternoon', 'part_of_speech': 'noun'},
        ],
        'phrases': [
            "Good morning!",
            "Good afternoon!",
            "How are you today?",
        ]
    },
    # ... add more starter lessons here
]

def seed_lessons():
    lesson1 = Lesson(
        title = 'Pronouns'
        difficulty = 'Beginner'
        user_id = None
        description = " This is learning the Basics - 1"
    )