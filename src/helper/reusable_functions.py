from src.helper.requests_wrapper import RequestsWrapper
from src.constants.api_constants import APIConstant
from src.helper.payload_manager import PayloadManager
from src.utils.headers import Headers


def get_bookings():
    post_response = RequestsWrapper.get_request(url=APIConstant.get_all_bookings_url(),
                                                                  header=Headers.get_common_header())

    return post_response


def get_booking_by_id(booking_id):
    get_response = RequestsWrapper.get_request_by_id(url=APIConstant.get_booking_url_by_id(booking_id),
                                                     header=Headers.get_common_header())
    return get_response


def create_booking():
    payload = PayloadManager.payload_new_booking()
    post_response = RequestsWrapper.post_request(url=APIConstant.get_create_booking_url(),
                                                                  header=Headers.get_common_header(),
                                                                  payload=payload)
    return post_response, payload


def update_booking(booking_id,token):
    payload = PayloadManager.payload_update_booking()
    update_response = RequestsWrapper.put_request(url=APIConstant.get_update_booking_url(booking_id),
                                                  header = Headers.get_cookie_auth_header(token),
                                                  payload = payload)
    return update_response, payload


def delete_booking(booking_id,token):
    delete_response = RequestsWrapper.delete_request(url=APIConstant.get_delete_booking_url(booking_id),
                                                  header=Headers.get_cookie_auth_header(token))
    return delete_response