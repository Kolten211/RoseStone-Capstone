from app.models import db, User, Word, LearnedWord

def seed_demo_user_words():
    demo_user = User.query.filter_by(username='Demo').first()

    if demo_user:
        all_words = Word.query.all()
        
        LearnedWord.query.filter_by( user_id = demo_user.id).delete()
        db.session.commit()

        for word in all_words:
            learned_word = LearnedWord(user_id=demo_user.id, word_id=word.id)
            db.session.add(learned_word)

        db.session.commit()
        print("It Worked")

    else:
        print("Demo user not found. SKIPPED")

def undo_demo_user_words():
    demo_user = User.query.filter_by(username='Demo').first()
    if demo_user:
        LearnedWord.query.filter_by( user_id = demo_user.id).delete()
        db.session.commit()