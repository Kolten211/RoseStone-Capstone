import boto3
import botocore
import os



translate = boto3.client(
    'translate',
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
    region_name='us-west-2'
)

def translate_helper(text, source_lang, target_lang):
    try:
        response = translate.translate_text(
            Text=text,
            SourceLanguageCode=source_lang,
            TargetLanguageCode=target_lang
        )
        return response['TranslatedText']
    except Exception as e:
        return {"errors": str(e)}