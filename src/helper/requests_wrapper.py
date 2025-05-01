import requests
import json

""" this helper function is wrapper to all crud api requests """


class RequestsWrapper:

    @staticmethod
    def auth_request(url, header, payload):
        response = requests.post(url=url, headers=header, data=json.dumps(payload))
        return response


    @staticmethod
    def get_request(url, header):
        response = requests.get(url=url, headers=header)
        return response

    def get_request_by_id(url, header):
        response = requests.get(url=url, headers=header)
        return response

    @staticmethod
    def post_request(url, header, payload):
        response = requests.post(url=url, headers=header, data=json.dumps(payload))
        return response

    @staticmethod
    def put_request(url, header, payload):
        response = requests.put(url=url, headers=header, data=json.dumps(payload))
        return response

    @staticmethod
    def patch_request(url, header, payload):
        response = requests.patch(url=url, headers=header, data=json.dumps(payload))
        return response

    @staticmethod
    def delete_request(url, header):
        response = requests.delete(url=url, headers=header)
        return response

