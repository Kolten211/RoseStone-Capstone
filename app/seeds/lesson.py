from app.models import db, Lesson, Word, Phrase, environment, SCHEMA
from sqlalchemy.sql import text


def seed_lessons():

    words = [
    Word(word="I", translation="I", part_of_speech="Pronoun", learned=False),
    Word(word="me", translation="mE", part_of_speech="Pronoun", learned=False),
    Word(word="you", translation="U", part_of_speech="Pronoun", learned=False),
    Word(word="he", translation="hE", part_of_speech="Pronoun", learned=False),
    Word(word="she", translation="shE", part_of_speech="Pronoun", learned=False),
    Word(word="it", translation="it", part_of_speech="Pronoun", learned=False),
    Word(word="we", translation="wE", part_of_speech="Pronoun", learned=False),
    Word(word="they", translation="they", part_of_speech="Pronoun", learned=False),
    Word(word="my", translation="mI", part_of_speech="Possessive Pronoun", learned=False),
    Word(word="your", translation="yor", part_of_speech="Possessive Pronoun", learned=False),
    Word(word="his", translation="his", part_of_speech="Possessive Pronoun", learned=False),
    Word(word="her", translation="hr", part_of_speech="Possessive Pronoun", learned=False),
    Word(word="its", translation="its", part_of_speech="Possessive Pronoun", learned=False),
    Word(word="our", translation="our", part_of_speech="Possessive Pronoun", learned=False),
    Word(word="their", translation="thair", part_of_speech="Possessive Pronoun", learned=False),
    Word(word="big", translation="big", part_of_speech="Adjective", learned=False),
    Word(word="small", translation="smal", part_of_speech="Adjective", learned=False),
    Word(word="happy", translation="happE", part_of_speech="Adjective", learned=False),
    Word(word="sad", translation="sad", part_of_speech="Adjective", learned=False),
    Word(word="good", translation="good", part_of_speech="Adjective", learned=False),
    Word(word="bad", translation="bad", part_of_speech="Adjective", learned=False),
    Word(word="hot", translation="hot", part_of_speech="Adjective", learned=False),
    Word(word="cold", translation="kOld", part_of_speech="Adjective", learned=False),
    Word(word="new", translation="new", part_of_speech="Adjective", learned=False),
    Word(word="old", translation="Old", part_of_speech="Adjective", learned=False),
    Word(word="go", translation="gO", part_of_speech="Verb", learned=False),
    Word(word="come", translation="cum", part_of_speech="Verb", learned=False),
    Word(word="eat", translation="Et", part_of_speech="Verb", learned=False),
    Word(word="drink", translation="drEnk", part_of_speech="Verb", learned=False),
    Word(word="sleep", translation="slEp", part_of_speech="Verb", learned=False),
    Word(word="walk", translation="wok", part_of_speech="Verb", learned=False),
    Word(word="run", translation="run", part_of_speech="Verb", learned=False),
    Word(word="play", translation="plA", part_of_speech="Verb", learned=False),
    Word(word="work", translation="wrk", part_of_speech="Verb", learned=False),
    Word(word="study", translation="studE", part_of_speech="Verb", learned=False)
    ]
    db.session.add_all(words)
    db.session.commit()

    phrases = [
    Phrase(phrase="I am happy.", translation="I am happE.", learned=False),
    Phrase(phrase="You are tall.", translation="U R tal", learned=False),
    Phrase(phrase="He is a student.", translation="hE is A stewdent.", learned=False),
    Phrase(phrase="She is beautiful.", translation="shE is BUtiful.", learned=False),
    Phrase(phrase="It is a cat.", translation="it is A cat.", learned=False),
    Phrase(phrase="Where do you live?", translation="Ware doo U liv?", learned=False),
    Phrase(phrase="What is your name?", translation="Wat is yor name?", learned=False),
    Phrase(phrase="How are you?", translation="how R U?", learned=False),
    Phrase(phrase="Do you like coffee?", translation="do you lIk cofE?", learned=False),
    Phrase(phrase="Please and thank you.", translation="plEs and thank U.", learned=False),
    Phrase(phrase="Excuse me.", translation="ecsUs mE.", learned=False),
    Phrase(phrase="I don't understand.", translation="I dOn't undrstand.", learned=False),
    Phrase(phrase="Can you repeat that, please?", translation="can you rEPEt that, plEs?", learned=False),
    # Add more common phrases and expressions here
    ]

    db.session.add_all(phrases)
    db.session.commit()

    lesson1 = Lesson(
        title = 'Pronouns',
        difficulty = 'Beginner',
        user_id = None,
        description = " This is learning the Basics - 1"
    )
    lesson1.words.extend(words[0:13])

    lesson2 =Lesson(
        title = 'Verbs',
        difficulty = 'Beginner',
        user_id = None,
        description = " This is learning the Basics - 2"
    )
    lesson2.words.extend(words[24:])

    lesson3 = Lesson(
        title = 'Adjectives',
        difficulty = 'Beginner',
        user_id = None,
        description = " This is learning the Basics - 3"
    )
    lesson3.words.extend(words[14:23])

    lesson4 = Lesson(
        title = 'Etiquette',
        difficulty = 'Intermediate',
        user_id = None,
        description = " Learning to form Sentences - 1"  
    )
    lesson4.phrases.extend(phrases[9:])

    lesson5 = Lesson(
        title = 'Describe',
        difficulty = 'Intermediate',
        user_id = None,
        description = " Learning to form Sentences - 2" 
    )
    lesson5.phrases.extend(phrases[0:4])

    lesson6 = Lesson(
        title = 'Questions',
        difficulty = 'Intermediate',
        user_id = None,
        description = " Learning to form Sentences - 3" 
    )
    lesson6.phrases.extend(phrases[5:8])

    db.session.add(lesson1)
    db.session.add(lesson2)
    db.session.add(lesson3)
    db.session.add(lesson4)
    db.session.add(lesson5)
    db.session.add(lesson6)
    db.session.commit()

def undo_lessons():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.lessons RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.lessons_words RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.lessons_phrases RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.words RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.phrases RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM lessons"))
        db.session.execute(text("DELETE FROM lessons_words"))
        db.session.execute(text("DELETE FROM lessons_phrases"))
        db.session.execute(text("DELETE FROM words"))
        db.session.execute(text("DELETE FROM phrases"))
    
    db.session.commit()