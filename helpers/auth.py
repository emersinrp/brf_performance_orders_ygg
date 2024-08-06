import requests
import os

def get_authentication():
    url = os.getenv("AUTH_URL")
    client_id = os.getenv("CLIENT_ID")
    client_secret_header = os.getenv("CLIENT_SECRET_HEADER_AUTH")
    client_secret_payload_auth = os.getenv("CLIENT_SECRET_PAYLOAD_AUTH")
    auth_cookie = os.getenv("AUTH_COOKIE", '')

    if not client_secret_header:
        raise ValueError("CLIENT_SECRET is not set in the environment variables")

    payload = (
        f'client_id=operation&grant_type=client_credentials&client_secret={client_secret_payload_auth}&scope=openid')
    
    headers = {
        'client_id': client_id,
        'client_secret': client_secret_header,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': auth_cookie
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 401:
        print("Unauthorized: Check your CLIENT_SECRET and AUTH_COOKIE")
    response.raise_for_status()
    data = response.json()
    return f"{data['token_type']} {data['access_token']}"
