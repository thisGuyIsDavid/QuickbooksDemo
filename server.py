from flask import Flask
from flask import request, json
from app.auth import set_bearer_token
import json as python_json
#   To run, use "flask --app server run"

app = Flask(__name__)
AUTH_ENDPOINT = "https://appcenter.intuit.com/connect/oauth2"


@app.route("/")
def hello_world():
    #   Get authentication details from Intuit auth request.
    request_arguments = request.args
    intuit_code = request_arguments.get('code')
    intuit_realm_id = request_arguments.get('realmId')
    set_bearer_token(intuit_code, intuit_realm_id)
    return json.jsonify({'token_status': 'set'})

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)