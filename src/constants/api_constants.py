import requests

""" the module consists static methods to get endpoint urls for api crud tests"""


class APIConstant:

    @staticmethod
    def get_base_url():
        return "https://restful-booker.herokuapp.com/"


    @staticmethod
    def get_heathcheck_url():
        return APIConstant.get_base_url() + "ping"


    @staticmethod
    def get_auth_url():
        return APIConstant.get_base_url() + "auth"


    @staticmethod
    def get_all_bookings_url():
        return APIConstant.get_base_url() + "booking"


    @staticmethod
    def get_create_booking_url():
        return APIConstant.get_base_url() + "booking"


    @staticmethod
    def get_booking_url_by_id(booking_id):
        return APIConstant.get_base_url() + "booking/" + str(booking_id)


    @staticmethod
    def get_update_booking_url(booking_id):
        return  APIConstant.get_base_url() + "booking/" + str(booking_id)


    @staticmethod
    def get_delete_booking_url(booking_id):
        return APIConstant.get_base_url() + "booking/" + str(booking_id)
