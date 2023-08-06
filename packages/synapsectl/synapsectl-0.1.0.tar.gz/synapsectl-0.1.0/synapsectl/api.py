import synapsectl.config
import requests
import urllib.parse
import sys


def request(method, url, payload=None, auth=False, token=None):
    config = synapsectl.config.get_config()
    host = config.get('connection', 'url')
    url = urllib.parse.urljoin(host, url)

    headers = {}
    if auth and token is None:
        if not config.has_option('connection', 'token'):
            print("No access token set", file=sys.stderr)
            print("You can get an access token if your account has the admin flag set. The token", file=sys.stderr)
            print("should be visible in your client, in Element it's settings->help", file=sys.stderr)
            print("", file=sys.stderr)
            print("Save the access token with synapsectl set-token [token]", file=sys.stderr)
            sys.exit(1)
        headers['Authorization'] = 'Bearer {}'.format(config.get('connection', 'token'))
    if token:
        headers['Authorization'] = 'Bearer {}'.format(token)

    if method == 'post':
        response = requests.post(url, json=payload, headers=headers)
    elif method == 'get':
        response = requests.get(url, headers=headers)

    if response.status_code == 401:
        body = response.json()
        if 'errcode' in body and body['errcode'] == 'M_UNKNOWN_TOKEN':
            print("The supplied access token doesn't represent a valid user account", file=sys.stderr)
            sys.exit(1)

    return response
