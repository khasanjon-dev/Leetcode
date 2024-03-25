from pprint import pprint as print

import requests
import ujson

IIKO_BASE_URL = 'https://api-ru.iiko.services/api/1/'


def get_order_types(branch_id):
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiN2EyYjBiMjMtNDNiYi00YjU4LWE0NjAtNGVkMDc4NTY3MDFiIiwibmJmIjoxNzEwOTMyMzAxLCJleHAiOjE3MTA5MzU5MDEsImlhdCI6MTcxMDkzMjMwMSwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.wOfkqNLFLQ6AcxXLVrocals-AqsYQTX3ougxGs8KVjs'
    url = f'{IIKO_BASE_URL}deliveries/order_types'
    payload = ujson.dumps(
        {
            "organizationIds": [
                branch_id
            ]
        }
    )
    # token = cache.get('IIKO_TOKEN')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    # if response.status_code != 200:
    #     # token = get_token()
    #     headers['Authorization'] = f'Bearer {token}'
    #     response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        response = response.json()
        order_types = response['orderTypes'][0]['items']
        return order_types
    return response.status_code


print(get_order_types('c73ac1d0-1864-400f-a9fd-709ed1dad77c'))
