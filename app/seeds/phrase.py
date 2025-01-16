from app.models import db, Phrase, environment, SCHEMA
from sqlalchemy.sql import text

def seed_phrases():
    phrases = [
        Phrase(phrase="I am happy.", translation="Estoy feliz.", learned=False),
        Phrase(phrase="You are tall.", translation="Eres alto/a.", learned=False),
        Phrase(phrase="He is a student.", translation="Él es estudiante.", learned=False),
        Phrase(phrase="She is beautiful.", translation="Ella es hermosa.", learned=False),
        Phrase(phrase="It is a cat.", translation="Es un gato.", learned=False),
        Phrase(phrase="Where do you live?", translation="¿Dónde vives?", learned=False),
        Phrase(phrase="What is your name?", translation="¿Cómo te llamas?", learned=False),
        Phrase(phrase="How are you?", translation="¿Cómo estás?", learned=False),
        Phrase(phrase="Do you like coffee?", translation="¿Te gusta el café?", learned=False),
        Phrase(phrase="Please and thank you.", translation="Por favor y gracias.", learned=False),
        Phrase(phrase="Excuse me.", translation="Disculpe.", learned=False),
        Phrase(phrase="I don't understand.", translation="No entiendo.", learned=False),
        Phrase(phrase="Can you repeat that, please?", translation="¿Puede repetir eso, por favor?", learned=False),
        # Add more common phrases and expressions here
    ]
    db.session.add_all(phrases)
    db.session.commit()

def undo_phrases():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.phrases RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM phrases"))
    
db.session.commit()