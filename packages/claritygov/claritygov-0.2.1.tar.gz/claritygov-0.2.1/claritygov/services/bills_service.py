import json
from typing import *

import requests

from ..api_config import APIConfig, HTTPException
from ..models import *


def get_state_bills_by_session(
    state: str, year: str, api_config_override: Optional[APIConfig] = None
) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/{state}/bills/{year}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    response = requests.request(
        "get",
        f"{base_path}{path}",
        headers=headers,
        params=query_params,
        verify=api_config.verify,
    )
    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


def get_state_bills_by_year_chamber(
    state: str, year: str, chamber: str, api_config_override: Optional[APIConfig] = None
) -> Dict[str, Any]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/{state}/bills/{year}/{chamber}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    response = requests.request(
        "get",
        f"{base_path}{path}",
        headers=headers,
        params=query_params,
        verify=api_config.verify,
    )
    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return response.json()


def get_state_bill_by_year_chamber_bill_number(
    state: str, year: str, chamber: str, bill_number: str, api_config_override: Optional[APIConfig] = None
) -> Bill:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/{state}/bills/{year}/{chamber}/{bill_number}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer { api_config.get_access_token() }",
    }
    query_params: Dict[str, Any] = {}

    query_params = {key: value for (key, value) in query_params.items() if value is not None}

    response = requests.request(
        "get",
        f"{base_path}{path}",
        headers=headers,
        params=query_params,
        verify=api_config.verify,
    )
    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return Bill(**response.json()) if response.json() is not None else Bill()
