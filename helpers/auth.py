import requests
from datetime import datetime, timedelta


def get_authentication():
    url = "https://ygg-qas.brf.cloud/token"

    payload = ('client_id=operation&grant_type=client_credentials&client_secret=lyd5u0UYmsbQhFIiTwGjf4Uk0vSZhPGy&scope'
               '=openid')
    headers = {
        'client_id': 'financial',
        'client_secret': '17KcCvHtiqTTxmSzxjKYtnBylfZjnr6l',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'visid_incap_2849035=kxgVA4uDTI+ZucI9a3Dud+LOa2QAAAAAQUIPAAAAAACLiw8529l1QAxwv6n1/vyZ; '
                  'visid_incap_2927240=kXxG8zS3QHWHS6LYFBPLyCUji2QAAAAAQUIPAAAAAACCPFSv9P7NvxrlrjlZUUEw; '
                  'visid_incap_2849035=QjX/sH4SQR6koy2tfRfimedGf2QAAAAAQUIPAAAAAACui9L5PMATqGM3H9hysSb9; '
                  'visid_incap_2927240=x6AYxXvhT3qd5Gt75nWZB/jf22QAAAAAQUIPAAAAAADSVyPiIIfeSzLZwIXSGZTo'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    resposta = response.json()

    token_expires = datetime.now() + timedelta(seconds=resposta["expires_in"])

    return f'{resposta["token_type"]} {resposta["access_token"]}', token_expires

