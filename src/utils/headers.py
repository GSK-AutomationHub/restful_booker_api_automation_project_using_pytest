import requests

""" the utils consist of header founction of common, basic auth, token auth types """


class Headers:

    @staticmethod
    def get_common_header():
        return {
            "Content-Type": "application/json"
        }

    @staticmethod
    def get_basic_auth_header(auth_value):
        return {
            "Content-Type": "application/json",
            "Authorization": "Basic " + str(auth_value)
        }

    @staticmethod
    def get_cookie_auth_header(token):
        return {
            "Content-Type": "application/json",
            "cookie": "token=" + str(token)
        }
