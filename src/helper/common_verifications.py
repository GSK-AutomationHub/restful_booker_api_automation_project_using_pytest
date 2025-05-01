import requests
import json
import pytest
from jsonschema import validate

""" this helper function have common verification that can be used across all crud api testcases """


def verify_status_code(response, expected):
    return response.status_code == expected


def verify_id_not_None(id):
    return id is not None

def verify_id_is_alphanumeric(id):
    return str(id).isalnum()

def verify_response_key(key, expected_data):
    assert key == expected_data


def verify_json_key_not_none(key):
    return key is not None


def verify_json_key_gr_zero(key):
    return key > 0


def verify_response_delete(response):
    return "Created" in response

def verify_response_invalid_token_request(response):
    return "Bad credentials" in response

def validate_json_schema(response, schema):
    try:
        validate(instance=response, schema=schema)
    except Exception as e:
        pytest.fail("Failed: Json Schema Error")
        return False
    else:
        print("json schema has no errors")
        return True
    finally:
        print("json schema validation completed")
