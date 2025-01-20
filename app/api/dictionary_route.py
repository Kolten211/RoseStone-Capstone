from flask import Blueprint, request, jsonify
import requests
from flask_login import login_required, current_user
import os

API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')

dictionary_routes = Blueprint('dictionary', __name__)


def get_audio_url(audio, lang='en', country='us', format='mp3'):
    if audio.startswith('bix'):
        subdirectory = 'bix'
    elif audio.startswith('gg'):
        subdirectory = 'gg'
    elif audio[0].isdigit() or not audio[0].isalpha():
        subdirectory = "number"
    else:
        subdirectory = audio[0]

    return f"https://media.merriam-webster.com/audio/prons/{lang}/{country}/{format}/{subdirectory}/{audio}.{format}"





@dictionary_routes.route('/', methods=['POST'])
@login_required
def deff_lookup():
    data = request.get_json()

    word = data.get('word')

    if not word:
        return {"message": "Please provide a word."}
    
    response = requests.get(f"{API_URL}{word}?key={API_KEY}")

    if response.status_code != 200:
        return {"message": "Failed to fetch"}
    
    print("What is happening", response.text)
    data = response.json()

    entry = data[0]
    meta = entry.get('meta', {})
    hwi = entry.get('hwi', {})
    def_list = entry.get('def', [])

    pronunciation = [
        {
            'pronunciation': prs.get('mw'),
            'audio_url': get_audio_url(prs['sound']['audio']) if 'sound' in prs else None 
        }
        for prs in hwi.get('prs', [])
    ]

    extracted_data = {
        'id': meta.get('id', 'N/A'),
        'uuid': meta.get('uuid', "N/A"),
        'lang': meta.get('lang', 'N/A'),
        'src': meta.get('src', 'N/A'),
        'stems': meta.get('stems', []),
        'offensive': meta.get('offensive', False),
        'headword': hwi.get('hw', 'N/A'),
        'pronunciation': pronunciation,
        "definitions": [
            {
                'sense_number': sense[1].get('sn'),
                'texts': [dt[1] if isinstance(dt[1], str) else dt[1].get('t') for dt in sense[1].get('dt', [])]
            }
            for sseq_item in def_list
            for sense in sseq_item[0][1].get('sseq', [])
        ],
        'short_definitions': entry.get('shortdef', [])
    }
    return jsonify(extracted_data)

