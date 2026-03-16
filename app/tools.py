import requests
import json
from langchain.tools import tool

@tool
def fetch_api_endpoints(spec_path: str):
    """Parses the OpenAPI spec and returns a list of all endpoints."""
    with open(spec_path, 'r') as f:
        spec = json.load(f)
    return list(spec['paths'].keys())

@tool
def execute_security_test(url: str, method: str, payload: dict = None, headers: dict = None):
    """Executes an API call to check for security vulnerabilities like BOLA."""
    try:
        response = requests.request(method, url, json=payload, headers=headers)
        return {
            "status_code": response.status_code,
            "body": response.json() if response.status_code == 200 else response.text,
            "is_vulnerable": response.status_code == 200 # If we access another user's data, it's a fail
        }
    except Exception as e:
        return f"Request failed: {str(e)}"
