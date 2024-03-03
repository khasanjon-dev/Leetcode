import os
from pprint import pprint as print

import httpx
import ujson
from dotenv import load_dotenv

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiN2EyYjBiMjMtNDNiYi00YjU4LWE0NjAtNGVkMDc4NTY3MDFiIiwibmJmIjoxNzA5Mjg2OTU5LCJleHAiOjE3MDkyOTA1NTksImlhdCI6MTcwOTI4Njk1OSwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.EtpZPiAoiZr3Ykd5KqAe8OIoROBYsEPERDJ3C08HSeQ'
load_dotenv()
base_url = os.getenv('BASE_URL')

ORGANIZATION_ID = os.getenv('ORGANIZATION_ID')
START_REVISION = int(os.getenv('START_REVISION'))
API_LOGIN = os.getenv('API_LOGIN')


def get_token() -> str:
    url = f'{base_url}access_token'
    payload = ujson.dumps(
        {
            'apiLogin': API_LOGIN
        }
    )

    headers = {
        'Content-Type': 'application/json'
    }

    response = httpx.post(url, headers=headers, data=payload)
    return response.json()['token']


def get_categories_and_products() -> dict:
    token = get_token()
    url = f'{base_url}nomenclature'
    payload = ujson.dumps(
        {
            'organizationId': ORGANIZATION_ID,
            'startRevision': START_REVISION
        }
    )
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = httpx.post(url, headers=headers, data=payload)
    if response.status_code == 401:
        raise ValueError('Token xato!')
    return response.json()


def get_branches():
    token = get_token()
    url = f'{base_url}organizations'
    payload = ujson.dumps({
        "organizationIds": [
            "8cbd6b1b-d339-4613-8e3b-6dd8de51aa26"
        ],
        "returnAdditionalInfo": True,
        "includeDisabled": True,
        "returnExternalData": [
            "string"
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = httpx.post(url, headers=headers, data=payload)
    # if response.status_code == 200:
    #     response = response.json()
    #     data = {
    #         'uid': response.get('')
    #     }
    return response.json()


# print(get_branches()[0])
category = get_categories_and_products()['groups'][0]
print(category)
id = category.get('id')
name = category.get('name')
parent_id = category.get('parentGroup')
print(id)
print(name)
print(parent_id)
