from flask import Blueprint, request, jsonify
from aws_requests_auth.aws_auth import AWSRequestsAuth
import os 
import boto3
from urllib.parse import urlencode
import requests

AWS_REGION = 'us-east-1'
API_GATEWAY_ENDPOINT = ' https://5990bvii05.execute-api.us-east-1.amazonaws.com/prod/dictionary-api-lambda'

api_gateway_hostname = "5990bvii05.execute-api.us-east-1.amazonaws.com"

dictionary_routes = Blueprint('dictionary', __name__)


session = boto3.Session(
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
    region_name = AWS_REGION
)

# credentials = session.get_credentials().get_frozen_credentials()

credentials = session.get_credentials()
print(f"Access Key ID being used: {api_gateway_hostname}")
signer = AWSRequestsAuth(
    aws_region=AWS_REGION, 
    aws_access_key=credentials.access_key, 
    aws_secret_access_key=credentials.secret_key, 
    aws_token=credentials.token,
    aws_host=api_gateway_hostname,
    aws_service='execute-api'
    )

@dictionary_routes.route('/')
def get_dictionary_meaning():
    word = request.args.get('word')
    if not word:
        return {'error': 'Missing "word" parameter'}, 400
    
    # service = 'execute-api'
    # method = 'GET'
    params = {"word": word}
    url = f"{API_GATEWAY_ENDPOINT}?{urlencode(params)}"
    headers = {}

    try: 
        # signer = RequestSigner(
        #     service,
        #     AWS_REGION,
        #     credentials.access_key,
        #     credentials.secret_key,
        #     credentials.token
        # )

        # signed_url = signer.sign(
        #     method=method,
        #     url=url,
        #     params=params,
        #     headers=headers
        # )
        auth=signer

        response = requests.get(url, auth=auth, headers=headers)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}, 500
    except Exception as e:
        return {'error': 'An unexpected error occured'}, 500
