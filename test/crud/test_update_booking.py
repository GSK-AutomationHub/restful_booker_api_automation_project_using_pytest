import requests
import json
import pytest
import allure

from src.constants.api_constants import APIConstant
from src.helper.reusable_functions import *
from src.utils.custom_logger import LogsGenerator
from src.utils.headers import Headers
from src.helper.requests_wrapper import RequestsWrapper
from src.helper.common_verifications import *
from src.helper.payload_manager import PayloadManager
from src.utils.prop_reader import PropReader


class TestUpdateBooking:

    logger = LogsGenerator.get_logger()
    @pytest.mark.crud
    @allure.title("Verify Update Booking API request")
    @allure.description("Updating a Booking with updated payload & validate following"
                        " - http status code should be 200"
                        " - booking details should be correctly updated")
    @pytest.mark.order("fifth")
    def test_005_update_booking(self,create_token):

        print("########### TC-test_005_update_booking: test execution started ###########")
        self.logger.info("########### test_005_update_booking: test execution started ###########")

        # create booking
        post_response, create_payload = create_booking()
        post_response_data = post_response.json()
        booking_id = post_response_data["bookingid"]

        # update booking
        update_response, update_payload = update_booking(booking_id,create_token)
        schema = PropReader.read_json_file('update_booking_schema.json')

        # get booking
        get_response = get_booking_by_id(booking_id)
        get_response_data = get_response.json()

        # assertions
        assert verify_status_code(post_response, 200)
        assert verify_status_code(update_response, 200)
        assert verify_status_code(get_response, 200)
        assert validate_json_schema(update_response.json(), schema)
        assert get_response_data.get('firstname') == update_payload.get('firstname')
        assert get_response_data['totalprice'] == update_payload['totalprice']
        assert get_response_data['depositpaid'] == update_payload['depositpaid']
        assert get_response_data['additionalneeds'] == update_payload['additionalneeds']

        print("########### TC-test_005_update_booking: test execution completed ###########")
        self.logger.info("########### test_005_update_booking: test execution completed ###########")
