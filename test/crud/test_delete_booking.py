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


class TestDeleteBooking:

    logger = LogsGenerator.get_logger()
    @pytest.mark.crud
    @allure.title("Verify Delete Booking API request")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    @pytest.mark.order("sixth")
    def test_006_delete_booking(self, create_token):

        print("########### TC-test_006_delete_booking: test execution started ###########")
        self.logger.info("########### test_006_delete_booking: test execution started ###########")

        # create booking
        post_response, create_booking_payload = create_booking()
        post_response_data = post_response.json()
        booking_id = post_response_data["bookingid"]

        # delete booking
        delete_response = delete_booking(booking_id, create_token)

        # assertions
        assert verify_status_code(delete_response, 201)
        assert verify_response_delete(response=delete_response.text)

        # get booking post delete booking
        get_response_for_deleted_booking = get_booking_by_id(booking_id)
        # get_response_data_for_deleted_booking = get_response_for_deleted_booking.json()

        # assertions
        assert verify_status_code(response=get_response_for_deleted_booking, expected=404)

        print("########### test_006_delete_booking: test execution completed ###########")
        self.logger.info("########### test_006_delete_booking: test execution completed ###########")


