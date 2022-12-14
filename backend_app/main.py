from backend_app import webapp
import json
from botocore.config import Config

def get_response(input=False):
    if input:
        response = webapp.response_class(
            response=json.dumps("OK"),
            status=200,
            mimetype='application/json'
        )
    else:
        response = webapp.response_class(
            response=json.dumps("Bad Request"),
            status=400,
            mimetype='application/json'
        )

    return response

@webapp.route('/', methods=['GET', 'POST'])
def main():
    return get_response(True)