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


class TestGetBookingIDs:

    logger = LogsGenerator.get_logger()
    @pytest.mark.crud
    @allure.title("Verify fetching all Bookings with Get Request")
    @allure.description("verify fetching all bookings & validate following"
                        " - http status code should be 200"
                        " - response should be list and booking ids should not be null")
    @pytest.mark.order("second")
    def test_002_get_all_bookings(self):

        print("########### TC-test_002_get_all_bookings: test execution started ###########")
        self.logger.info("########### test_002_get_all_bookings: test execution started ###########")

        # create booking
        get_response = get_bookings()
        booking_id = get_response.json()[0]["bookingid"]

        # assertions
        assert verify_status_code(get_response, 200)
        assert type(get_response.json()) is list
        assert verify_id_not_None(booking_id)
        assert verify_id_is_alphanumeric(booking_id)

        print("########### TC-test_002_get_all_bookings: test execution completed ###########")
        self.logger.info("########### test_002_get_all_bookings: test execution completed ###########")

