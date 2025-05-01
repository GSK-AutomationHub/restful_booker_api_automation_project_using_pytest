import pytest
import requests
from src.constants.api_constants import APIConstant
from src.utils.custom_logger import LogsGenerator
from src.helper.common_verifications import verify_status_code

@pytest.mark.order("first")
def test_001_booker_api_health_check():
    logger = LogsGenerator.get_logger()
    print("########### TC-test_001_booker_api_health_check: test execution started ###########")
    logger.info("########### test_001_booker_api_health_check: test execution started ###########")

    health_check_response = requests.get(url=APIConstant.get_heathcheck_url())
    print(f"health checkup response code is - {health_check_response.status_code}")
    assert verify_status_code (health_check_response, 201)

    print("########### TC-test_001_booker_api_health_check: test execution completed ###########")
    logger.info("########### test_001_booker_api_health_check: test execution completed ###########")