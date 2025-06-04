import json
from app.models import db, Lesson, Word, Phrase, Question, Answer, environment, SCHEMA
from sqlalchemy.sql import text


def seed_lessons():

    words = [
    Word(word="I", translation="Yo", part_of_speech="Pronoun", audio_url=""),
    Word(word="me", translation="Me", part_of_speech="Pronoun", audio_url=""),
    Word(word="you", translation="tú", part_of_speech="Pronoun", audio_url=""),
    Word(word="he", translation="él", part_of_speech="Pronoun", audio_url=""),
    Word(word="she", translation="ella", part_of_speech="Pronoun", audio_url=""),
    Word(word="it", translation="lo", part_of_speech="Pronoun", audio_url=""),
    Word(word="we", translation="nosotros", part_of_speech="Pronoun", audio_url=""),
    Word(word="they", translation="ellos, ellas", part_of_speech="Pronoun", audio_url=""),
    Word(word="cat", translation="gato", part_of_speech="Noun", audio_url=""),
    Word(word="name", translation="nombre", part_of_speech="Noun", audio_url=""),
    Word(word="coffee", translation="café", part_of_speech="Noun", audio_url=""),
    Word(word="student", translation="estudiante", part_of_speech="Noun", audio_url=""),
    Word(word="my", translation="mi", part_of_speech="Possessive Pronoun"),
    Word(word="your", translation="tu", part_of_speech="Possessive Pronoun", audio_url=""),
    Word(word="his", translation="su, el suyo", part_of_speech="Possessive Pronoun", audio_url=""),
    Word(word="her", translation="ella", part_of_speech="Possessive Pronoun", audio_url=""),
    Word(word="its", translation="su, sus", part_of_speech="Possessive Pronoun", audio_url=""),
    Word(word="our", translation="nuestro", part_of_speech="Possessive Pronoun", audio_url=""),
    Word(word="their", translation="su, sus", part_of_speech="Possessive Pronoun", audio_url=""),
    Word(word="big", translation="grande", part_of_speech="Adjective", audio_url=""),
    Word(word="small", translation="pequeño", part_of_speech="Adjective", audio_url=""),
    Word(word="happy", translation="feliz", part_of_speech="Adjective", audio_url=""),
    Word(word="sad", translation="triste", part_of_speech="Adjective", audio_url=""),
    Word(word="good", translation="bueno", part_of_speech="Adjective", audio_url=""),
    Word(word="bad", translation="malo, mal", part_of_speech="Adjective", audio_url=""),
    Word(word="hot", translation="caliente", part_of_speech="Adjective", audio_url=""),
    Word(word="cold", translation="frio", part_of_speech="Adjective", audio_url=""),
    Word(word="new", translation="nuvo", part_of_speech="Adjective", audio_url=""),
    Word(word="old", translation="viejo", part_of_speech="Adjective", audio_url=""),
    Word(word="tall", translation="alto", part_of_speech="Adjective", audio_url=""),
    Word(word="beautiful", translation="hermoso", part_of_speech="Adjective", audio_url=""),
    Word(word="please", translation="por favor", part_of_speech="Interjection", audio_url=""),
    Word(word="excuse", translation="disculpar", part_of_speech="Interjection", audio_url=""),
    Word(word="and", translation="y", part_of_speech="Conjunction", audio_url=""),
    Word(word="thank", translation="agradecer", part_of_speech="Verb", audio_url=""),
    Word(word="go", translation="ir", part_of_speech="Verb", audio_url=""),
    Word(word="come", translation="venir", part_of_speech="Verb", audio_url=""),
    Word(word="eat", translation="comer", part_of_speech="Verb", audio_url=""),
    Word(word="drink", translation="beber", part_of_speech="Verb", audio_url=""),
    Word(word="sleep", translation="dormir", part_of_speech="Verb", audio_url=""),
    Word(word="walk", translation="caminar", part_of_speech="Verb", audio_url=""),
    Word(word="run", translation="correr", part_of_speech="Verb", audio_url=""),
    Word(word="play", translation="jugar", part_of_speech="Verb", audio_url=""),
    Word(word="work", translation="trabajar, manejar, hacer", part_of_speech="Verb", audio_url=""),
    Word(word="study", translation="el estudio", part_of_speech="Verb", audio_url=""),
    Word(word="am", translation="ser", part_of_speech="Verb", audio_url=""),
    Word(word="do", translation="hacer", part_of_speech="Verb", audio_url=""),
    Word(word="understand", translation="entender, comprender", part_of_speech="Verb", audio_url=""),
    Word(word="repeat", translation="repetir", part_of_speech="Verb", audio_url=""),
    Word(word="not", translation="no", part_of_speech="", audio_url=""),
    Word(word="can", translation="poder, saber", part_of_speech="Verb", audio_url=""),
    Word(word="like", translation="gustar", part_of_speech="Verb", audio_url=""),
    Word(word="live", translation="viver", part_of_speech="Verb", audio_url=""),
    Word(word="a", translation="un, ", part_of_speech="Article", audio_url=""),
    Word(word="that", translation="que, eso, ese", part_of_speech="Adverb", audio_url=""),
    Word(word="what", translation="qué", part_of_speech="Adverb", audio_url=""),
    Word(word="where", translation="dónde", part_of_speech="Adverb", audio_url=""),
    Word(word="how", translation="cómo", part_of_speech="Adverb", audio_url=""),
    Word(word="the", translation="", part_of_speech="", audio_url=""),
    Word(word="be", translation="", part_of_speech="", audio_url=""),
    Word(word="of", translation="", part_of_speech="", audio_url=""),
    Word(word="in", translation="", part_of_speech="", audio_url=""),
    Word(word="to", translation="", part_of_speech="", audio_url=""),
    Word(word="have", translation="", part_of_speech="", audio_url=""),
    Word(word="create", translation="", part_of_speech="", audio_url=""),
    Word(word="for", translation="", part_of_speech="", audio_url=""),
    Word(word="with", translation="", part_of_speech="", audio_url=""),
    Word(word="on", translation="", part_of_speech="", audio_url=""),
    Word(word="say", translation="", part_of_speech="", audio_url=""),
    Word(word="this", translation="", part_of_speech="", audio_url=""),
    Word(word="us", translation="", part_of_speech="", audio_url=""),
    Word(word="at", translation="", part_of_speech="", audio_url=""),
    Word(word="but", translation="", part_of_speech="", audio_url=""),
    Word(word="nice", translation="", part_of_speech="", audio_url=""),
    Word(word="add", translation="", part_of_speech="", audio_url=""),
    Word(word="from", translation="", part_of_speech="", audio_url=""),
    Word(word="favorite", translation="", part_of_speech="", audio_url=""),
    Word(word="by", translation="", part_of_speech="", audio_url=""),
    Word(word="mom", translation="", part_of_speech="", audio_url=""),
    Word(word="or", translation="", part_of_speech="", audio_url=""),
    Word(word="grandpa", translation="", part_of_speech="", audio_url=""),
    Word(word="brother", translation="", part_of_speech="", audio_url=""),
    Word(word="dad", translation="", part_of_speech="", audio_url=""),
    Word(word="who", translation="", part_of_speech="", audio_url=""),
    Word(word="get", translation="", part_of_speech="", audio_url=""),
    Word(word="if", translation="", part_of_speech="", audio_url=""),
    Word(word="would", translation="", part_of_speech="", audio_url=""),
    Word(word="sister", translation="", part_of_speech="", audio_url=""),
    Word(word="pretty", translation="", part_of_speech="", audio_url=""),
    Word(word="make", translation="", part_of_speech="", audio_url=""),
    Word(word="about", translation="", part_of_speech="", audio_url=""),
    Word(word="know", translation="", part_of_speech="", audio_url=""),
    Word(word="will", translation="", part_of_speech="", audio_url=""),
    Word(word="up", translation="", part_of_speech="", audio_url=""),
    Word(word="one", translation="", part_of_speech="", audio_url=""),
    Word(word="time", translation="", part_of_speech="", audio_url=""),
    Word(word="there", translation="", part_of_speech="", audio_url=""),
    Word(word="year", translation="", part_of_speech="", audio_url=""),
    Word(word="so", translation="", part_of_speech="", audio_url=""),
    Word(word="think", translation="", part_of_speech="", audio_url=""),
    Word(word="dog", translation="", part_of_speech="", audio_url=""),
    Word(word="which", translation="", part_of_speech="", audio_url=""),
    Word(word="them", translation="", part_of_speech="", audio_url=""),
    Word(word="some", translation="", part_of_speech="", audio_url=""),
    Word(word="people", translation="", part_of_speech="", audio_url=""),
    Word(word="take", translation="", part_of_speech="", audio_url=""),
    Word(word="out", translation="", part_of_speech="", audio_url=""),
    Word(word="into", translation="", part_of_speech="", audio_url=""),
    Word(word="just", translation="", part_of_speech="", audio_url=""),
    Word(word="see", translation="", part_of_speech="", audio_url=""),
    Word(word="him", translation="", part_of_speech="", audio_url=""),
    Word(word="now", translation="", part_of_speech="", audio_url=""),
    Word(word="could", translation="", part_of_speech="", audio_url=""),
    Word(word="than", translation="", part_of_speech="", audio_url=""),
    Word(word="other", translation="", part_of_speech="", audio_url=""),
    Word(word="then", translation="", part_of_speech="", audio_url=""),
    Word(word="two", translation="", part_of_speech="", audio_url=""),
    Word(word="more", translation="", part_of_speech="", audio_url=""),
    Word(word="these", translation="", part_of_speech="", audio_url=""),
    Word(word="want", translation="", part_of_speech="", audio_url=""),
    Word(word="way", translation="", part_of_speech="", audio_url=""),
    Word(word="look", translation="", part_of_speech="", audio_url=""),
    Word(word="first", translation="", part_of_speech="", audio_url=""),
    Word(word="also", translation="", part_of_speech="", audio_url=""),
    Word(word="son", translation="", part_of_speech="", audio_url=""),
    Word(word="because", translation="", part_of_speech="", audio_url=""),
    Word(word="day", translation="", part_of_speech="", audio_url=""),
    Word(word="use", translation="", part_of_speech="", audio_url=""),
    Word(word="no", translation="", part_of_speech="", audio_url=""),
    Word(word="man", translation="", part_of_speech="", audio_url=""),
    Word(word="girl", translation="", part_of_speech="", audio_url=""),
    Word(word="find", translation="", part_of_speech="", audio_url=""),
    Word(word="here", translation="", part_of_speech="", audio_url=""),
    Word(word="thing", translation="", part_of_speech="", audio_url=""),
    Word(word="give", translation="", part_of_speech="", audio_url=""),
    Word(word="many", translation="", part_of_speech="", audio_url=""),
    Word(word="well", translation="", part_of_speech="", audio_url=""),
    Word(word="only", translation="", part_of_speech="", audio_url=""),
    Word(word="those", translation="", part_of_speech="", audio_url=""),
    Word(word="tell", translation="", part_of_speech="", audio_url=""),
    Word(word="boy", translation="", part_of_speech="", audio_url=""),
    Word(word="woman", translation="", part_of_speech="", audio_url=""),
    Word(word="even", translation="", part_of_speech="", audio_url=""),
    Word(word="back", translation="", part_of_speech="", audio_url=""),
    Word(word="any", translation="", part_of_speech="", audio_url=""),
    Word(word="daughter", translation="", part_of_speech="", audio_url=""),
    Word(word="grandma", translation="", part_of_speech="", audio_url=""),
    Word(word="life", translation="", part_of_speech="", audio_url=""),
    Word(word="child", translation="", part_of_speech="", audio_url=""),
    Word(word="they're", translation="", part_of_speech="", audio_url=""),
    Word(word="interview", translation="", part_of_speech="", audio_url=""),
    Word(word="down", translation="", part_of_speech="", audio_url=""),
    Word(word="may", translation="", part_of_speech="", audio_url=""),
    Word(word="after", translation="", part_of_speech="", audio_url=""),
    Word(word="before", translation="", part_of_speech="", audio_url=""),
    Word(word="should", translation="", part_of_speech="", audio_url=""),
    Word(word="wood", translation="", part_of_speech="", audio_url=""),
    Word(word="morning", translation="", part_of_speech="", audio_url=""),
    Word(word="afternoon", translation="", part_of_speech="", audio_url=""),
    Word(word="food", translation="", part_of_speech="", audio_url=""),
    Word(word="school", translation="", part_of_speech="", audio_url=""),
    Word(word="call", translation="", part_of_speech="", audio_url=""),
    Word(word="world", translation="", part_of_speech="", audio_url=""),
    Word(word="hello", translation="", part_of_speech="", audio_url=""),
    Word(word="hi", translation="", part_of_speech="", audio_url=""),
    Word(word="later", translation="", part_of_speech="", audio_url=""),
    Word(word="meet", translation="", part_of_speech="", audio_url=""),
    Word(word="still", translation="", part_of_speech="", audio_url=""),
    Word(word="try", translation="", part_of_speech="", audio_url=""),
    Word(word="as", translation="", part_of_speech="", audio_url=""),
    Word(word="last", translation="", part_of_speech="", audio_url=""),
    Word(word="ask", translation="", part_of_speech="", audio_url=""),
    Word(word="need", translation="", part_of_speech="", audio_url=""),
    Word(word="too", translation="", part_of_speech="", audio_url=""),
    Word(word="feel", translation="", part_of_speech="", audio_url=""),
    Word(word="three", translation="", part_of_speech="", audio_url=""),
    Word(word="second", translation="", part_of_speech="", audio_url=""),
    Word(word="when", translation="", part_of_speech="", audio_url=""),
    Word(word="state", translation="", part_of_speech="", audio_url=""),
    Word(word="never", translation="", part_of_speech="", audio_url=""),
    Word(word="become", translation="", part_of_speech="", audio_url=""),
    Word(word="between", translation="", part_of_speech="", audio_url=""),
    Word(word="high", translation="", part_of_speech="", audio_url=""),
    Word(word="really", translation="", part_of_speech="", audio_url=""),
    Word(word="something", translation="", part_of_speech="", audio_url=""),
    Word(word="most", translation="", part_of_speech="", audio_url=""),
    Word(word="another", translation="", part_of_speech="", audio_url=""),
    Word(word="much", translation="", part_of_speech="", audio_url=""),
    Word(word="family", translation="", part_of_speech="", audio_url=""),
    Word(word="own", translation="", part_of_speech="", audio_url=""),
    Word(word="pet", translation="", part_of_speech="", audio_url=""),
    Word(word="leave", translation="", part_of_speech="", audio_url=""),
    Word(word="put", translation="", part_of_speech="", audio_url=""),
    Word(word="young", translation="", part_of_speech="", audio_url=""),
    Word(word="while", translation="", part_of_speech="", audio_url=""),
    Word(word="mean", translation="", part_of_speech="", audio_url=""),
    Word(word="keep", translation="", part_of_speech="", audio_url=""),
    Word(word="let", translation="", part_of_speech="", audio_url=""),
    Word(word="great", translation="", part_of_speech="", audio_url=""),
    Word(word="seem", translation="", part_of_speech="", audio_url=""),
    Word(word="group", translation="", part_of_speech="", audio_url=""),
    Word(word="hand", translation="", part_of_speech="", audio_url=""),
    Word(word="talk", translation="", part_of_speech="", audio_url=""),
    Word(word="every", translation="", part_of_speech="", audio_url=""),
    Word(word="American", translation="", part_of_speech="", audio_url=""),
    Word(word="show", translation="", part_of_speech="", audio_url=""),
    Word(word="part", translation="", part_of_speech="", audio_url=""),
    Word(word="might", translation="", part_of_speech=""),
    Word(word="against", translation="", part_of_speech="", audio_url=""),
    Word(word="place", translation="", part_of_speech="", audio_url=""),
    Word(word="over", translation="", part_of_speech="", audio_url=""),
    Word(word="such", translation="", part_of_speech="", audio_url=""),
    Word(word="again", translation="", part_of_speech="", audio_url=""),
    Word(word="each", translation="", part_of_speech="", audio_url=""),
    Word(word="tight", translation="", part_of_speech="", audio_url=""),
    Word(word="program", translation="", part_of_speech="", audio_url=""),
    Word(word="doctor", translation="", part_of_speech="", audio_url=""),
    Word(word="color", translation="", part_of_speech="", audio_url=""),
    Word(word="case", translation="", part_of_speech="", audio_url=""),
    Word(word="maid", translation="", part_of_speech="", audio_url=""),
    Word(word="question", translation="", part_of_speech="", audio_url=""),
    Word(word="during", translation="", part_of_speech="", audio_url=""),
    Word(word="grocery", translation="", part_of_speech="", audio_url=""),
    Word(word="store", translation="", part_of_speech="", audio_url=""),
    Word(word="number", translation="", part_of_speech="", audio_url=""),
    Word(word="hospital", translation="", part_of_speech="", audio_url=""),
    Word(word="hurt", translation="", part_of_speech="", audio_url=""),
    Word(word="pain", translation="", part_of_speech="", audio_url=""),
    Word(word="bathroom", translation="", part_of_speech="", audio_url=""),
    Word(word="taxi", translation="", part_of_speech="", audio_url=""),
    Word(word="pharmacy", translation="", part_of_speech="", audio_url=""),
    Word(word="government", translation="", part_of_speech="", audio_url=""),
    Word(word="help", translation="", part_of_speech="", audio_url=""),
    Word(word="country", translation="", part_of_speech="", audio_url=""),
    Word(word="turn", translation="", part_of_speech="", audio_url=""),
    Word(word="problem", translation="", part_of_speech="", audio_url=""),
    Word(word="start", translation="", part_of_speech="", audio_url=""),
    Word(word="end", translation="", part_of_speech="", audio_url=""),
    Word(word="few", translation="", part_of_speech="", audio_url=""),
    Word(word="lucky", translation="", part_of_speech="", audio_url=""),
    Word(word="bird", translation="", part_of_speech="", audio_url=""),
    Word(word="mad", translation="", part_of_speech="", audio_url=""),
    Word(word="hat", translation="", part_of_speech="", audio_url=""),
    Word(word="off", translation="", part_of_speech="", audio_url=""),
    Word(word="always", translation="", part_of_speech="", audio_url=""),
    Word(word="move", translation="", part_of_speech="", audio_url=""),
    Word(word="stay", translation="", part_of_speech="", audio_url=""),
    Word(word="night", translation="", part_of_speech="", audio_url=""),
    Word(word="cool", translation="", part_of_speech="", audio_url=""),
    Word(word="Mr.", translation="", part_of_speech="", audio_url=""),
    Word(word="point", translation="", part_of_speech="", audio_url=""),
    Word(word="believe", translation="", part_of_speech="", audio_url=""),
    Word(word="hold", translation="", part_of_speech="", audio_url=""),
    Word(word="today", translation="", part_of_speech="", audio_url=""),
    Word(word="tomorrow", translation="", part_of_speech="", audio_url=""),
    Word(word="large", translation="", part_of_speech="", audio_url=""),
    Word(word="all", translation="", part_of_speech="", audio_url=""),
    Word(word="must", translation="", part_of_speech="", audio_url=""),
    Word(word="bring", translation="", part_of_speech="", audio_url=""),
    Word(word="happen", translation="", part_of_speech="", audio_url=""),
    Word(word="next", translation="", part_of_speech="", audio_url=""),
    Word(word="without", translation="", part_of_speech="", audio_url=""),
    Word(word="ice", translation="", part_of_speech="", audio_url=""),
    Word(word="under", translation="", part_of_speech="", audio_url=""),
    Word(word="water", translation="", part_of_speech="", audio_url=""),
    Word(word="room", translation="", part_of_speech="", audio_url=""),
    Word(word="write", translation="", part_of_speech="", audio_url=""),
    Word(word="mother", translation="", part_of_speech="", audio_url=""),
    Word(word="speak", translation="", part_of_speech="", audio_url=""),
    Word(word="area", translation="", part_of_speech="", audio_url=""),
    Word(word="father", translation="", part_of_speech="", audio_url=""),
    Word(word="national", translation="", part_of_speech="", audio_url=""),
    Word(word="money", translation="", part_of_speech="", audio_url=""),
    Word(word="story", translation="", part_of_speech="", audio_url=""),
    Word(word="fact", translation="", part_of_speech="", audio_url=""),
    Word(word="month", translation="", part_of_speech="", audio_url=""),
    Word(word="right", translation="", part_of_speech="", audio_url=""),
    Word(word="book", translation="", part_of_speech="", audio_url=""),
    Word(word="eye", translation="", part_of_speech="", audio_url=""),
    Word(word="job", translation="", part_of_speech="", audio_url=""),
    Word(word="word", translation="", part_of_speech="", audio_url=""),
    Word(word="though", translation="", part_of_speech="", audio_url=""),
    Word(word="business", translation="", part_of_speech="", audio_url=""),
    Word(word="issue", translation="", part_of_speech="", audio_url=""),
    Word(word="side", translation="", part_of_speech="", audio_url=""),
    Word(word="kind", translation="", part_of_speech="", audio_url=""),
    Word(word="long", translation="", part_of_speech="", audio_url=""),
    Word(word="short", translation="", part_of_speech="", audio_url=""),
    Word(word="both", translation="", part_of_speech="", audio_url=""),
    Word(word="won", translation="", part_of_speech="", audio_url=""),
    Word(word="little", translation="", part_of_speech="", audio_url=""),
    Word(word="house", translation="", part_of_speech="", audio_url=""),
    Word(word="home", translation="", part_of_speech="", audio_url=""),
    Word(word="yes", translation="", part_of_speech="", audio_url=""),
    Word(word="friend", translation="", part_of_speech="", audio_url=""),
    Word(word="Monday", translation="", part_of_speech="", audio_url=""),
    Word(word="Tuesday", translation="", part_of_speech="", audio_url=""),
    Word(word="Wednesday", translation="", part_of_speech="", audio_url=""),
    Word(word="Thursday", translation="", part_of_speech="", audio_url=""),
    Word(word="Friday", translation="", part_of_speech="", audio_url=""),
    Word(word="Saturday", translation="", part_of_speech="", audio_url=""),
    Word(word="Sunday", translation="", part_of_speech="", audio_url=""),
    Word(word="stand", translation="", part_of_speech="", audio_url=""),
    Word(word="sit", translation="", part_of_speech="", audio_url=""),
    Word(word="jump", translation="", part_of_speech="", audio_url=""),
    Word(word="crawl", translation="", part_of_speech="", audio_url=""),
    Word(word="smart", translation="", part_of_speech="", audio_url=""),
    Word(word="brush", translation="", part_of_speech="", audio_url=""),
    Word(word="self", translation="", part_of_speech="", audio_url=""),
    Word(word="important", translation="", part_of_speech="", audio_url=""),
    Word(word="line", translation="", part_of_speech="", audio_url=""),
    Word(word="snow", translation="", part_of_speech="", audio_url=""),
    Word(word="service", translation="", part_of_speech="", audio_url=""),
    Word(word="provide", translation="", part_of_speech="", audio_url=""),
    Word(word="law", translation="", part_of_speech="", audio_url=""),
    Word(word="city", translation="", part_of_speech="", audio_url=""),
    Word(word="car", translation="", part_of_speech="", audio_url=""),
    Word(word="truck", translation="", part_of_speech="", audio_url=""),
    Word(word="president", translation="", part_of_speech="", audio_url=""),
    Word(word="learn", translation="", part_of_speech="", audio_url=""),
    Word(word="drive", translation="", part_of_speech="", audio_url=""),
    Word(word="real", translation="", part_of_speech="", audio_url=""),
    Word(word="fake", translation="", part_of_speech="", audio_url=""),
    Word(word="news", translation="", part_of_speech="", audio_url=""),
    Word(word="change", translation="", part_of_speech="", audio_url=""),
    Word(word="include", translation="", part_of_speech="", audio_url=""),
    Word(word="dinner", translation="", part_of_speech="", audio_url=""),
    Word(word="buy", translation="", part_of_speech="", audio_url="")
    ]
    db.session.add_all(words)
    db.session.commit()

    phrases = [
    Phrase(phrase="I am happy.", translation=""),
    Phrase(phrase="You are tall.", translation=""),
    Phrase(phrase="He is a student.", translation=""),
    Phrase(phrase="She is beautiful.", translation=""),
    Phrase(phrase="It is a cat.", translation=""),
    Phrase(phrase="Where do you live?", translation=""),
    Phrase(phrase="What is your name?", translation=""),
    Phrase(phrase="How are you?", translation=""),
    Phrase(phrase="Do you like coffee?", translation=""),
    Phrase(phrase="Please and thank you.", translation=""),
    Phrase(phrase="Excuse me.", translation=""),
    Phrase(phrase="I don't understand.", translation=""),
    Phrase(phrase="Can you repeat that, please?", translation=""),
    # Add more common phrases and expressions here
    ]

    db.session.add_all(phrases)
    db.session.commit()

    lesson1_questions = [
        Question(
            question_text='Qué escuchas',
            audio_file='',
            word_id=db.session.query(Word).filter_by(word='I').first().id,
            answers = [
                Answer(answer_text='eye', is_correct=True),
                Answer(answer_text='ai', is_correct=True),
                Answer(answer_text='I', is_correct=True),
                Answer(answer_text='A', is_correct=False)
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='me').first().id,
            answers = [
                Answer(answer_text='mee', is_correct=True),
                Answer(answer_text='mea', is_correct=True),
                Answer(answer_text='mii', is_correct=True),
                Answer(answer_text='me', is_correct=True)
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='you').first().id,
            answers = [
                Answer(answer_text='u', is_correct=True),
                Answer(answer_text='you', is_correct=True),
                Answer(answer_text='yew', is_correct=True),
                Answer(answer_text='yu', is_correct=True),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='he').first().id,
            answers = [
                Answer(answer_text='he', is_correct=True),
                Answer(answer_text='hee', is_correct=True),
                Answer(answer_text='hay', is_correct=True),
                Answer(answer_text='hard', is_correct=False),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='she').first().id,
            answers = [
                Answer(answer_text='shee', is_correct=True),
                Answer(answer_text='shi', is_correct=True),
                Answer(answer_text='she', is_correct=True),
                Answer(answer_text='them', is_correct=False),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='it').first().id,
            answers = [
                Answer(answer_text='it', is_correct=True),
                Answer(answer_text='lip', is_correct=False),
                Answer(answer_text='et', is_correct=True),
                Answer(answer_text='cape', is_correct=False),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='we').first().id,
            answers = [
                Answer(answer_text='wii', is_correct=True),
                Answer(answer_text='whee', is_correct=True),
                Answer(answer_text='we', is_correct=True),
                Answer(answer_text='hi', is_correct=False),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='they').first().id,
            answers = [
                Answer(answer_text='thay', is_correct=True),
                Answer(answer_text='thae', is_correct=True),
                Answer(answer_text='theigh', is_correct=True),
                Answer(answer_text='they', is_correct=True),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='his').first().id,
            answers = [
                Answer(answer_text='hiz', is_correct=True),
                Answer(answer_text='hiss', is_correct=True),
                Answer(answer_text='hez', is_correct=True),
                Answer(answer_text='his', is_correct=True),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='her').first().id,
            answers = [
                Answer(answer_text='hur', is_correct=True),
                Answer(answer_text='him', is_correct=False),
                Answer(answer_text='her', is_correct=True),
                Answer(answer_text='hurr', is_correct=True),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='its').first().id,
            answers = [
                Answer(answer_text='itz', is_correct=True),
                Answer(answer_text='its', is_correct=True),
                Answer(answer_text='ritz', is_correct=False),
                Answer(answer_text='this', is_correct=False),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='our').first().id,
            answers = [
                Answer(answer_text='owr', is_correct=True),
                Answer(answer_text='hour', is_correct=True),
                Answer(answer_text='our', is_correct=True),
                Answer(answer_text='ower', is_correct=True),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='their').first().id,
            answers = [
                Answer(answer_text='thair', is_correct=True),
                Answer(answer_text='thayer', is_correct=True),
                Answer(answer_text='thare', is_correct=True),
                Answer(answer_text='their', is_correct=True),
            ]
        ),  

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='cat').first().id,
            answers = [
                Answer(answer_text='kat', is_correct=True),
                Answer(answer_text='cat', is_correct=True),
                Answer(answer_text='kate', is_correct=False),
                Answer(answer_text='cape', is_correct=False),
            ]
        ),

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='name').first().id,
            answers = [
                Answer(answer_text='name', is_correct=True),
                Answer(answer_text='naim', is_correct=True),
                Answer(answer_text='nape', is_correct=False),
                Answer(answer_text='fame', is_correct=False),
            ]
        ), 

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='coffee').first().id,
            answers = [
                Answer(answer_text='coughee', is_correct=True),
                Answer(answer_text='coffe', is_correct=True),
                Answer(answer_text='cofe', is_correct=True),
                Answer(answer_text='coffee', is_correct=True),
            ]
        ), 

        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='student').first().id,
            answers = [
                Answer(answer_text='student', is_correct=True),
                Answer(answer_text='coffee', is_correct=False),
                Answer(answer_text='name', is_correct=False),
                Answer(answer_text='stewdant', is_correct=True),
            ]
        ),   
    ]

    lesson2_questions = [
                Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='thank').first().id,
            answers = [
                Answer(answer_text='thank', is_correct=True),
                Answer(answer_text='hank', is_correct=True),
                Answer(answer_text='shank', is_correct=False),
                Answer(answer_text='bank', is_correct=False),
            ]
        ),
                Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='go').first().id,
            answers = [
                Answer(answer_text='Joe', is_correct=False),
                Answer(answer_text='throw', is_correct=False),
                Answer(answer_text='bow', is_correct=False),
                Answer(answer_text='go', is_correct=True),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='come').first().id,
            answers = [
                Answer(answer_text='fun', is_correct=False),
                Answer(answer_text='come', is_correct=True),
                Answer(answer_text='thumb', is_correct=False),
                Answer(answer_text='shun', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='eat').first().id,
            answers = [
                Answer(answer_text='feet', is_correct=False),
                Answer(answer_text='sheep', is_correct=False),
                Answer(answer_text='beep', is_correct=False),
                Answer(answer_text='eat', is_correct=True),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='drink').first().id,
            answers = [
                Answer(answer_text='sink', is_correct=False),
                Answer(answer_text='drink', is_correct=True),
                Answer(answer_text='plink', is_correct=False),
                Answer(answer_text='clink', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='sleep').first().id,
            answers = [
                Answer(answer_text='sleep', is_correct=True),
                Answer(answer_text='sheep', is_correct=False),
                Answer(answer_text='beep', is_correct=False),
                Answer(answer_text='feet', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='walk').first().id,
            answers = [
                Answer(answer_text='stalk', is_correct=False),
                Answer(answer_text='talk', is_correct=False),
                Answer(answer_text='watt', is_correct=False),
                Answer(answer_text='walk', is_correct=True),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='run').first().id,
            answers = [
                Answer(answer_text='bun', is_correct=False),
                Answer(answer_text='run', is_correct=True),
                Answer(answer_text='sun', is_correct=False),
                Answer(answer_text='gun', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='play').first().id,
            answers = [
                Answer(answer_text='slay', is_correct=False),
                Answer(answer_text='fei', is_correct=False),
                Answer(answer_text='play', is_correct=True),
                Answer(answer_text='clay', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='work').first().id,
            answers = [
                Answer(answer_text='work', is_correct=True),
                Answer(answer_text='were', is_correct=False),
                Answer(answer_text='wok', is_correct=False),
                Answer(answer_text='slice', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='study').first().id,
            answers = [
                Answer(answer_text='study', is_correct=True),
                Answer(answer_text='spud', is_correct=False),
                Answer(answer_text='muddy', is_correct=False),
                Answer(answer_text='funny', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='am').first().id,
            answers = [
                Answer(answer_text='ham', is_correct=False),
                Answer(answer_text='sham', is_correct=False),
                Answer(answer_text='slam', is_correct=False),
                Answer(answer_text='am', is_correct=True),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='do').first().id,
            answers = [
                Answer(answer_text='do', is_correct=True),
                Answer(answer_text='show', is_correct=False),
                Answer(answer_text='few', is_correct=False),
                Answer(answer_text='crew', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='understand').first().id,
            answers = [
                Answer(answer_text='understand', is_correct=True),
                Answer(answer_text='slumber', is_correct=False),
                Answer(answer_text='blunder', is_correct=False),
                Answer(answer_text='thunder', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='repeat').first().id,
            answers = [
                Answer(answer_text='repeat', is_correct=True),
                Answer(answer_text='seat', is_correct=False),
                Answer(answer_text='creep', is_correct=False),
                Answer(answer_text='concrete', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='not').first().id,
            answers = [
                Answer(answer_text='not', is_correct=True),
                Answer(answer_text='cop', is_correct=False),
                Answer(answer_text='stop', is_correct=False),
                Answer(answer_text='tot', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='can').first().id,
            answers = [
                Answer(answer_text='fan', is_correct=False),
                Answer(answer_text='can', is_correct=True),
                Answer(answer_text='slam', is_correct=False),
                Answer(answer_text='van', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='like').first().id,
            answers = [
                Answer(answer_text='bike', is_correct=False),
                Answer(answer_text='kite', is_correct=False),
                Answer(answer_text='pike', is_correct=False),
                Answer(answer_text='like', is_correct=True),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='live').first().id,
            answers = [
                Answer(answer_text='live', is_correct=True),
                Answer(answer_text='life', is_correct=False),
                Answer(answer_text='light', is_correct=False),
                Answer(answer_text='sight', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='a').first().id,
            answers = [
                Answer(answer_text='a', is_correct=True),
                Answer(answer_text='to', is_correct=False),
                Answer(answer_text='ate', is_correct=False),
                Answer(answer_text='bait', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='that').first().id,
            answers = [
                Answer(answer_text='this', is_correct=False),
                Answer(answer_text='bat', is_correct=False),
                Answer(answer_text='cat', is_correct=False),
                Answer(answer_text='that', is_correct=True),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='what').first().id,
            answers = [
                Answer(answer_text='when', is_correct=False),
                Answer(answer_text='where', is_correct=False),
                Answer(answer_text='weather', is_correct=False),
                Answer(answer_text='what', is_correct=True),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='where').first().id,
            answers = [
                Answer(answer_text='here', is_correct=False),
                Answer(answer_text='there', is_correct=False),
                Answer(answer_text='where', is_correct=True),
                Answer(answer_text='sear', is_correct=False),
            ]
        ),
        Question(
            question_text = 'Qué escuchas',
            audio_file = '',
            word_id = db.session.query(Word).filter_by(word='how').first().id,
            answers = [
                Answer(answer_text='cow', is_correct=False),
                Answer(answer_text='plow', is_correct=False),
                Answer(answer_text='loud', is_correct=False),
                Answer(answer_text='how', is_correct=True),
            ]
        ),
    ]

    lesson1 = Lesson(
        title = 'Pronouns',
        difficulty = 'Beginner',
        user_id = None,
        description = "This is learning the Basics - 1"
    )
    lesson1.words.extend(words[0:18])
    lesson1.questions.extend(lesson1_questions)

    lesson2 =Lesson(
        title = 'Verbs',
        difficulty = 'Beginner',
        user_id = None,
        description = "This is learning the Basics - 2"
    )
    lesson2.words.extend(words[34:57])
    lesson2.questions.extend(lesson2_questions)

    lesson3 = Lesson(
        title = 'Adjectives',
        difficulty = 'Beginner',
        user_id = None,
        description = "This is learning the Basics - 3"
    )
    lesson3.words.extend(words[19:33])

    lesson4 = Lesson(
        title = 'Etiquette',
        difficulty = 'Intermediate',
        user_id = None,
        description = "Learning to form Sentences - 1"  
    )
    lesson4.phrases.extend(phrases[9:])

    lesson5 = Lesson(
        title = 'Describe',
        difficulty = 'Intermediate',
        user_id = None,
        description = "Learning to form Sentences - 2" 
    )
    lesson5.phrases.extend(phrases[0:4])

    lesson6 = Lesson(
        title = 'Questions',
        difficulty = 'Intermediate',
        user_id = None,
        description = "Learning to form Sentences - 3" 
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
        db.session.execute(f"TRUNCATE table {SCHEMA}.questions RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.answers RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.lesson_question RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.learned_words RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.learned_phrases RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM lessons"))
        db.session.execute(text("DELETE FROM lessons_words"))
        db.session.execute(text("DELETE FROM lessons_phrases"))
        db.session.execute(text("DELETE FROM words"))
        db.session.execute(text("DELETE FROM phrases"))
        db.session.execute(text("DELETE FROM questions"))
        db.session.execute(text("DELETE FROM answers"))
        db.session.execute(text("DELETE FROM lesson_question"))
        db.session.execute(text("DELETE FROM learned_phrases"))
        db.session.execute(text("DELETE FROM learned_words"))
    
    db.session.commit()

def seed_data():
    seed_users()