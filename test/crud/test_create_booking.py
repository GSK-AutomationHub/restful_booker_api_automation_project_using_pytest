import requests
import json
import pytest
import allure

from src.constants.api_constants import APIConstant
from src.helper.reusable_functions import *
from src.utils.custom_logger import LogsGenerator
from src.utils.headers import Headers
from src.utils.prop_reader import PropReader
from src.helper.requests_wrapper import RequestsWrapper
from src.helper.common_verifications import *
from src.helper.payload_manager import PayloadManager



class TestCreateBooking:

    logger = LogsGenerator.get_logger()
    @pytest.mark.crud
    @allure.title("Verify Create Booking API request")
    @allure.description("Creating a Booking from the payload & validate following"
                        " - http status code should be 200"
                        " - booking id should not be null")
    @pytest.mark.order("fourth")
    def test_004_create_booking(self):

        print("########### TC-test_004_create_booking: test execution started ###########")
        self.logger.info("########### test_004_create_booking: test execution started ###########")

        # create booking
        post_response, payload = create_booking()
        post_response_data = post_response.json()
        booking_id = post_response_data["bookingid"]
        schema = PropReader.read_json_file('create_booking_schema.json')

        # get booking
        get_response = get_booking_by_id(booking_id)
        get_response_data = get_response.json()

        # assertions
        assert verify_status_code(post_response,200)
        assert "booking" in post_response_data
        assert verify_id_not_None(post_response_data["bookingid"])
        assert verify_id_is_alphanumeric(post_response_data["bookingid"])
        assert validate_json_schema(post_response.json(), schema)
        assert verify_status_code(get_response, 200)
        assert get_response_data.get('firstname') == payload.get('firstname')
        assert get_response_data['totalprice'] == payload['totalprice']

        print("########### TC-test_004_create_booking: test execution completed ###########")
        self.logger.info("########### test_004_create_booking: test execution completed ###########")
