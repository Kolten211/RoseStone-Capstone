from app.models import db, Word, environment, SCHEMA
from sqlalchemy.sql import text

def seed_words():
  words = [
        Word(word="I", part_of_speech="Pronoun", learned=False),
        Word(word="me", part_of_speech="Pronoun", learned=False),
        Word(word="you", part_of_speech="Pronoun", learned=False),
        Word(word="he", part_of_speech="Pronoun", learned=False),
        Word(word="she", part_of_speech="Pronoun", learned=False),
        Word(word="it", part_of_speech="Pronoun", learned=False),
        Word(word="we", part_of_speech="Pronoun", learned=False),
        Word(word="they", part_of_speech="Pronoun", learned=False),
        Word(word="my", part_of_speech="Possessive Pronoun", learned=False),
        Word(word="your", part_of_speech="Possessive Pronoun", learned=False),
        Word(word="his", part_of_speech="Possessive Pronoun", learned=False),
        Word(word="her", part_of_speech="Possessive Pronoun", learned=False),
        Word(word="its", part_of_speech="Possessive Pronoun", learned=False),
        Word(word="our", part_of_speech="Possessive Pronoun", learned=False),
        Word(word="their", part_of_speech="Possessive Pronoun", learned=False),
        Word(word="big", part_of_speech="Adjective", learned=False),
        Word(word="small", part_of_speech="Adjective", learned=False),
        Word(word="happy", part_of_speech="Adjective", learned=False),
        Word(word="sad", part_of_speech="Adjective", learned=False),
        Word(word="good", part_of_speech="Adjective", learned=False),
        Word(word="bad", part_of_speech="Adjective", learned=False),
        Word(word="hot", part_of_speech="Adjective", learned=False),
        Word(word="cold", part_of_speech="Adjective", learned=False),
        Word(word="new", part_of_speech="Adjective", learned=False),
        Word(word="old", part_of_speech="Adjective", learned=False),
        Word(word="go", part_of_speech="Verb", learned=False),
        Word(word="come", part_of_speech="Verb", learned=False),
        Word(word="eat", part_of_speech="Verb", learned=False),
        Word(word="drink", part_of_speech="Verb", learned=False),
        Word(word="sleep", part_of_speech="Verb", learned=False),
        Word(word="walk", part_of_speech="Verb", learned=False),
        Word(word="run", part_of_speech="Verb", learned=False),
        Word(word="play", part_of_speech="Verb", learned=False),
        Word(word="work", part_of_speech="Verb", learned=False),
        Word(word="study", part_of_speech="Verb", learned=False)
  ]
  db.session.add_all(words)
  db.session.commit()




def undo_words():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.words RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM words"))
        
    db.session.commit()