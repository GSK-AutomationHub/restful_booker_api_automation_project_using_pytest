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


class TestGetBooking:

    logger = LogsGenerator.get_logger()
    @pytest.mark.crud
    @allure.title("Verify fetching all Bookings with Get Request")
    @allure.description("verify fetching all bookings & validate following"
                        " - http status code should be 200"
                        " - response should be list and booking ids should not be null")
    @pytest.mark.order("third")
    def test_003_get_specific_booking_by_id(self):

        print("########### TC-test_003_get_specific_booking_by_id: test execution started ###########")
        self.logger.info("########### test_003_get_specific_booking_by_id: test execution started ###########")

        # create booking
        get_all_booking_ids_response = get_bookings()
        booking_id = get_all_booking_ids_response.json()[0]["bookingid"]
        get_booking_by_id_response = get_booking_by_id(booking_id)
        get_booking_by_id_response_data = get_booking_by_id_response.json()
        schema = PropReader.read_json_file('get_booking_schema.json')

        # assertions
        assert verify_status_code(get_booking_by_id_response, 200)
        assert validate_json_schema(get_booking_by_id_response.json(), schema)

        print("########### TC-test_003_get_specific_booking_by_id: test execution completed ###########")
        self.logger.info("########### test_003_get_specific_booking_by_id: test execution completed ###########")



