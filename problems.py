import os

import httpx
import ujson
from dotenv import load_dotenv

load_dotenv()
base_url = 'https://api-ru.iiko.services/api/1/'

ORGANIZATION_ID = os.getenv('ORGANIZATION_ID')
START_REVISION = int(os.getenv('START_REVISION'))
API_LOGIN = os.getenv('API_LOGIN')


# token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiN2EyYjBiMjMtNDNiYi00YjU4LWE0NjAtNGVkMDc4NTY3MDFiIiwibmJmIjoxNzA5MTg2NjM2LCJleHAiOjE3MDkxOTAyMzYsImlhdCI6MTcwOTE4NjYzNiwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.eE85r_dixWu8qQ6Ii4pPuCMSzd-Kl1F4Q2nJwZR6N3E'


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


def get_categories():
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiN2EyYjBiMjMtNDNiYi00YjU4LWE0NjAtNGVkMDc4NTY3MDFiIiwibmJmIjoxNzA5MTk0MzQxLCJleHAiOjE3MDkxOTc5NDEsImlhdCI6MTcwOTE5NDM0MSwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.ra6TujJ16i6QsHZKzjp9j2_AvvHbxj66NIIh66ZncF4'  # get_token()
    url = f'{base_url}nomenclature'
    payload = ujson.dumps(
        {
            "organizationId": ORGANIZATION_ID,
            "startRevision": START_REVISION
        }
    )
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = httpx.post(url, headers=headers, data=payload)
    if response.status_code == 401:
        raise Exception('error')
    print(response.json()['groups'])


get_categories()
