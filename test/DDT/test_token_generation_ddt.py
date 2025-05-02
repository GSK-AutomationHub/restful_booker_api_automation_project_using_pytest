import pytest

from src.constants.api_constants import APIConstant
from src.helper.common_verifications import *
from src.helper.requests_wrapper import RequestsWrapper
from src.utils.headers import Headers
from src.utils.excel_reader import *


class TestTokenGenerationDDT:

    Invalid_credentials = [
        ('admin', 'password'),  # valid username, invalid password
        ('non-admin', 'password123'),  # invalid username, valid password
        ('non-admin', 'password'),  # both invalid
        ('', '')  # both blank
    ]

    @pytest.mark.DDT
    @pytest.mark.parametrize("username,password", Invalid_credentials)
    def test_token_generation_ddt(self, username, password):
        auth_response = RequestsWrapper.auth_request(url=APIConstant.get_auth_url(),
                                                     header=Headers.get_common_header(),
                                                     payload={"username": username,
                                                              "password": password
                                                              })

        assert verify_status_code(response=auth_response, expected=200)
        assert verify_response_invalid_token_request(auth_response.json())


