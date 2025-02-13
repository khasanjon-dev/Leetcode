import base64
import json
import os
import time

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()

ORG_USERNAME = os.environ.get("ORG_USERNAME")
ORG_PASSWORD = os.environ.get("ORG_PASSWORD")
ORG_GRANT_TYPE = os.environ.get("ORG_GRANT_TYPE")
ORG_TOKEN_URL = os.environ.get("ORG_TOKEN_URL")
ORG_CONSUMER_KEY = os.environ.get("ORG_CONSUMER_KEY")
ORG_CONSUMER_SECRET = os.environ.get("ORG_CONSUMER_SECRET")
ORG_COMPANY_URL = os.environ.get("ORG_COMPANY_URL")

cache = {}


def get_token() -> dict | str:
    """Get authentication token and cache it."""
    if "org_token" in cache and cache["org_token"]["expires_at"] > time.time():
        return cache["org_token"]["token"]

    payload = {
        "grant_type": ORG_GRANT_TYPE,
        "username": ORG_USERNAME,
        "password": ORG_PASSWORD,
    }
    auth_str = f"{ORG_CONSUMER_KEY}:{ORG_CONSUMER_SECRET}"
    auth_base64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {auth_base64}",
    }
    try:
        response = requests.post(ORG_TOKEN_URL, headers=headers, data=payload)
        response.raise_for_status()
        token = response.json().get("access_token")
        expires_in = response.json().get("expires_in", 3600)  # Standart 1 soat

        if token:
            cache["org_token"] = {
                "token": token,
                "expires_at": time.time() + expires_in  # Token muddati
            }
        return token
    except RequestException as e:
        return {"error": "Failed to obtain token", "details": str(e)}


def get_company(inn: int | str) -> dict:
    """Fetch company details by INN from an external service."""
    payload = json.dumps({"tin": str(inn)})

    token = get_token()
    if isinstance(token, dict):
        return token

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.post(ORG_COMPANY_URL, headers=headers, data=payload)
        if response.status_code == 401:
            token = get_token()
            if isinstance(token, dict):
                return token

            headers["Authorization"] = f"Bearer {token}"
            response = requests.post(ORG_COMPANY_URL, headers=headers, data=payload)

        response.raise_for_status()
        response_js = response.json()
        return {
            "name": response_js.get("name"),
            "address": response_js.get("address"),
            "oked": response_js.get("nc6Code"),
            "ns_code": response_js.get("ns10Code"),
        }

    except RequestException as e:
        return {"error": "Failed to fetch company details", "details": str(e)}


print(get_company("200524845"))
