import requests
from faker import Faker

""" this helper function have common verification that can be used across all crud api testcases """


class PayloadManager:
    faker = Faker()

    @staticmethod
    def payload_new_booking():
        return {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-02-15",
                "checkout": "2025-02-18"
            },
            "additionalneeds": "Breakfast"
        }

    @staticmethod
    def payload_update_booking():
        return {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 525,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2025-02-10",
                "checkout": "2025-02-15"
            },
            "additionalneeds": "Parking"
        }

    @staticmethod
    def payload_dynamic(self):
        return {
            "firstname": self.faker.first_name(),
            "lastname": self.faker.last_name(),
            "totalprice": self.faker.random_int(min=100,max=1000),
            "depositpaid": self.faker.boolean(),
            "bookingdates": {
                "checkin": self.faker.date_between(start_date="2025-02-10",end_date="2025-02-15"),
                "checkout": self.faker.date_between(start_date="2025-02-15",end_date="2025-02-25")
            },
            "additionalneeds": self.faker.random_element(elements=("breakfast","parking","wifi","gym"))
        }

    @staticmethod
    def payload_from_excel(self):
        pass

    @staticmethod
    def payload_from_db(self):
        pass