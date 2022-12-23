"""
Client for Backend REST API.
"""

import os
from pathlib import Path
from typing import List

import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent.parent.parent.parent / '.env')


class BackendClient(object):
    """
    Client for the Backend REST API.
    """

    def __init__(self, hostname: str = None, port: str = None):
        """
        Creates a new client instance.

        Args:
            hostname (str or None): hostname for the Backend REST API.
                If None, BACKEND_HOSTNAME environment variable is used.
            port (str or None): port for the Backend REST API.
                If None, BACKEND_PORT environment variable is used.

        Returns: ('BackendClient') a new client instance.
        """
        self.hostname = hostname if hostname else os.getenv('BACKEND_HOSTNAME')
        self.port = port if port else os.getenv('BACKEND_PORT')
        self.API_URL = f'http://{self.hostname}:{self.port}/api/v0'

    def fetch_users(self) -> List[dict]:
        """
        Fetch list of app' users from the Backend REST API.

        Returns: (List[dict]) list of users
        """
        response = requests.get(
            url=f'{self.API_URL}/fetch_users',
            headers={'content-type': 'application/json'}
        )
        response.raise_for_status()
        return response.json()

    def fetch_data(self, user_id: int) -> List[dict]:
        """
        Fetch some data from the Backend REST API.

        Args:
            user_id (int): user id

        Returns: (List[dict]) list of measurements
        """
        response = requests.get(
            url=f'{self.API_URL}/fetch_user_measurements',
            headers={'content-type': 'application/json'},
            params=dict(user_id=user_id)
        )
        response.raise_for_status()
        return response.json()

    def process_data(self, user_id: int, measurements: List[dict], **kwargs):
        """
        Process data.

        Args:
            user_id (int): user id
            measurements (List[str]): list of measurements
            **kwargs: key-worded arguments to be sent as query params

        Returns: (dict) some processed data
        """
        input_json = {
            'user_id': user_id,
            'measurements': measurements
        }
        response = requests.post(
            url=f'{self.API_URL}/process',
            headers={'content-type': 'application/json'},
            json=input_json,
            params=kwargs
        )
        response.raise_for_status()
        return response.json()
