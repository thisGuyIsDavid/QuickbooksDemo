import json
import os

from intuitlib.client import AuthClient
from intuitlib.enums import Scopes

auth_info = json.load(open('../auth.json'))


CLIENT_ID = auth_info.get('CLIENT_ID')
CLIENT_SECRET = auth_info.get('CLIENT_SECRET')


def generate_url() -> None:
    """
    Using the provided CLIENT_ID and CLIENT SECRET, create and print an auth code for Intuit.
    :return: None.
    """
    auth_client = AuthClient(
        CLIENT_ID,
        CLIENT_SECRET,
        "http://localhost:5001",
        "sandbox"
    )
    scopes = [
        Scopes.ACCOUNTING,
    ]
    auth_url = auth_client.get_authorization_url(scopes)

    print(auth_url)


def set_bearer_token(auth_code:str, realm_id:str):
    auth_client = AuthClient(
        CLIENT_ID,
        CLIENT_SECRET,
        "http://localhost:5001",
        "sandbox"
    )
    auth_client.get_bearer_token(auth_code=auth_code, realm_id=realm_id)
    json.dump({'bearer_token': auth_client.access_token, 'realm_id': realm_id}, open('intuit_auth.json', 'w'))


def get_intuit_auth() -> json:
    if not os.path.exists('../intuit_auth.json'):
        raise FileNotFoundError('Please initiate the auth json first.')
    auth_file = json.load(open('../intuit_auth.json'))
    return auth_file

#   set_bearer_token('AB11677066537zObOEAsCDJcqCdAueNs3MMBL5OTX6KcdCBYb1', '4620816365282714010')