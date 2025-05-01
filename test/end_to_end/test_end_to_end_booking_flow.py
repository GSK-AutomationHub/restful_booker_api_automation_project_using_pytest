import allure
import pytest
from src.constants.api_constants import APIConstant
from src.helper.requests_wrapper import *
from src.helper.common_verifications import *
from src.helper.payload_manager import *
from src.helper.reusable_functions import *
from src.utils.custom_logger import LogsGenerator
from src.utils.prop_reader import PropReader


class TestE2E(object):

    logger = LogsGenerator.get_logger()

    @pytest.mark.e2e
    @allure.title("E2E Booking flow- Create -> Update -> Delete Booking)")
    @allure.description("Verify user could able to create, update, delete booking | Full CRUD")
    def test_end_to_end_booking_flow(self, create_token):
        print("########### TC-test_end_to_end_booking_flow: test execution started ###########")
        self.logger.info("########### TC-test_004_create_booking: test execution started ###########")
        print("########### new booking creation ###########")
        self.logger.info("########### new booking creation ###########")
        # create booking
        post_response, create_booking_payload = create_booking()
        post_response_data = post_response.json()
        booking_id = post_response_data["bookingid"]
        create_booking_schema = PropReader.read_json_file('create_booking_schema.json')

        print("########### getting the booking details ###########")
        self.logger.info("########### getting the booking details ###########")
        # get booking post creating booking
        get_response_for_created_booking = get_booking_by_id(booking_id)
        get_response_data_for_created_booking = get_response_for_created_booking.json()

        print("########### running create booking assertions ###########")
        self.logger.info("########### running create booking assertions ###########")
        # assertions for create booking
        assert verify_status_code(post_response, 200)
        assert "booking" in post_response_data
        assert verify_id_not_None(post_response_data["bookingid"])
        assert verify_id_is_alphanumeric(post_response_data["bookingid"])
        assert verify_status_code(get_response_for_created_booking, 200)
        assert get_response_data_for_created_booking.get('firstname') == create_booking_payload.get('firstname')
        assert get_response_data_for_created_booking['totalprice'] == create_booking_payload['totalprice']
        assert get_response_data_for_created_booking['depositpaid'] == create_booking_payload['depositpaid']
        assert get_response_data_for_created_booking['additionalneeds'] == create_booking_payload['additionalneeds']
        assert validate_json_schema(post_response.json(), create_booking_schema)

        print("########### updating the booking details ###########")
        self.logger.info("########### updating the booking details ###########")
        # update booking
        update_response, update_booking_payload = update_booking(booking_id,create_token)
        update_booking_schema = PropReader.read_json_file('update_booking_schema.json')

        print("########### getting the booking details post updating ###########")
        self.logger.info("########### getting the booking details post updating ###########")
        # get booking post update booking
        get_response_for_updated_booking = get_booking_by_id(booking_id)
        get_response_data_for_updated_booking = get_response_for_updated_booking.json()

        print("########### running update booking assertions ###########")
        self.logger.info("########### running update booking assertions ###########")
        # assertions
        assert verify_status_code(update_response, 200)
        assert verify_status_code(get_response_for_updated_booking, 200)
        assert get_response_data_for_updated_booking.get('firstname') == update_booking_payload.get('firstname')
        assert get_response_data_for_updated_booking['totalprice'] == update_booking_payload['totalprice']
        assert get_response_data_for_updated_booking['depositpaid'] == update_booking_payload['depositpaid']
        assert get_response_data_for_updated_booking['additionalneeds'] == update_booking_payload['additionalneeds']
        assert validate_json_schema(update_response.json(), update_booking_schema)

        print("########### deleting the booking  ###########")
        self.logger.info("########### deleting the booking ###########")
        # delete booking
        delete_response = delete_booking(booking_id,create_token)

        print("########### running delete booking assertions ###########")
        self.logger.info("########### running delete booking assertions ###########")
        # assertions
        assert verify_status_code(delete_response, 201)
        assert verify_response_delete(response=delete_response.text)

        # get booking post delete booking
        get_response_for_deleted_booking = get_booking_by_id(booking_id)

        # assertions
        assert verify_status_code(response=get_response_for_deleted_booking, expected=404)

        print("########### TC-test_end_to_end_booking_flow: test execution started: test execution completed ###########")
        self.logger.info("########### TC-test_end_to_end_booking_flow: test execution started: test execution completed ###########")

