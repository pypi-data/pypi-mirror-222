import json
from typing import *

import requests

from ..api_config import APIConfig, HTTPException
from ..models import *


def get_state_house_members(state: str, api_config_override: Optional[APIConfig] = None) -> List[Delegate]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/{state}/house/members"
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

    return [Delegate(**item) for item in response.json()]


def get_state_senators(state: str, api_config_override: Optional[APIConfig] = None) -> List[Senator]:
    api_config = api_config_override if api_config_override else APIConfig()

    base_path = api_config.base_path
    path = f"/{state}/senate/senators"
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

    return [Senator(**item) for item in response.json()]
