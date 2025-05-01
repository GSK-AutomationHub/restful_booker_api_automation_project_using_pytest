import pytest
from src.constants.api_constants import APIConstant
from src.helper.requests_wrapper import RequestsWrapper
from src.helper.common_verifications import *
from src.helper.reusable_functions import *
from src.utils.headers import Headers
from src.utils.prop_reader import PropReader


@pytest.fixture(scope="session")
def create_token():
    auth_response = RequestsWrapper.auth_request(url=APIConstant.get_auth_url(),
                                                 header=Headers.get_common_header(),
                                                 payload=PropReader.read_env_file())

    verify_status_code(response=auth_response, expected=200)
    print(auth_response.json())
    verify_json_key_not_none(auth_response.json()["token"])
    return auth_response.json()["token"]

# @pytest.fixture(scope="session")
# def get_booking_id():
#     post_response, create_booking_payload = create_booking()
#     booking_id = post_response.json()["bookingid"]
#     verify_status_code(response=post_response, expected=200)
#     verify_id_not_None(booking_id)
#     verify_id_is_alphanumeric(booking_id)
#     return booking_id