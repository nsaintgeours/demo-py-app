"""
Script that sends sample requests to the Backend REST API.
"""

import json

import pkg_resources
import requests

API_URL = 'http://localhost:8088/api/v0'

# Load sample input data
sample_json = pkg_resources.resource_filename('backend', 'resources/sample_input_data.json')
with open(sample_json, 'r') as f:
    sample_json = json.load(f)

# Send 'fetch_users' request to the Backend REST API
response = requests.get(url=f'{API_URL}/fetch_users')
response.raise_for_status()
print(response.json())

# Send 'fetch_user_measurements' request to the Backend REST API
response = requests.get(url=f'{API_URL}/fetch_user_measurements', params=dict(user_id=1))
response.raise_for_status()
print(response.json())

# Send 'process' request to the Backend REST API
response = requests.post(url=f'{API_URL}/process', json=sample_json, params=dict(some_param=0.78))
response.raise_for_status()
print(response.json())
