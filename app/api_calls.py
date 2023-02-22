from app.auth import get_intuit_auth
import requests
import json
INTUIT_URL = 'https://sandbox-quickbooks.api.intuit.com'


def get_request(endpoint_prefix: str, endpoint_suffix):
    intuit_auth_details = get_intuit_auth()
    response = requests.get(
        INTUIT_URL + endpoint_prefix + intuit_auth_details.get('realm_id') + endpoint_suffix,
        headers={
            'Authorization':'Bearer ' + intuit_auth_details.get('bearer_token'),
            'Accept': 'application/json'
        }
    )
    return response.json()


def post_request(endpoint_prefix: str, endpoint_suffix: str, post_object: dict) -> json:
    """
    :param endpoint_prefix: URL, minus the base URL ('https://sandbox-quickbooks.api.intuit.com') before REALM_ID.
    :param endpoint_suffix: URL after REALM_ID
    :param post_object: object to post
    :return: json response
    """
    intuit_auth_details = get_intuit_auth()
    response = requests.post(
        INTUIT_URL + endpoint_prefix + intuit_auth_details.get('realm_id') + endpoint_suffix,
        headers={
            'Authorization':'Bearer ' + intuit_auth_details.get('bearer_token'),
            'Accept': 'application/json'
        },
        json=post_object
    )
    return response.json()


def create_customer(company_object: dict) -> json:
    return post_request("/v3/company/", "/customer?minorversion=65", company_object)


def get_customer(customer_id: int) -> json:
    return get_request('/v3/company/', '/customer/' + str(customer_id) + '?minorversion=65')


def query_customers(query: str) -> json:
    return get_request('/v3/company/', '/query?query=' + query + '&minorversion=65')


def create_invoice(invoice_object: dict) -> json:
    return post_request("/v3/company/", "/invoice?minorversion=65", invoice_object)
