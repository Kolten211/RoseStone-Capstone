from flask import Blueprint, request
from flask_login import login_required
from app.api.aws_translate_helper import translate_helper

translate_routes = Blueprint('translate', __name__)

@translate_routes.route('/', methods=['POST'])
@login_required
def translate_text():

    data = request.get_json()
    text = data.get('text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')

    if not text or not source_lang or not target_lang:
        return {"errors": "Missing required fields"}, 400
    
    translated_text = translate_helper(text, source_lang, target_lang)

    if 'errors' in translated_text:
        return {"error": translated_text}, 500
    
    return {"translated_text": translated_text}