import logging
import os
from datetime import time

import pytest

from pages.login_page import LoginPage
from utils.driver_manager import WebDriverSingleton


def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"logs/test_execution_{time.strftime('%Y%m%d_%H%M%S')}.log"),
            logging.StreamHandler()
        ]
    )

@pytest.fixture(scope="session", autouse=True)
def initialize_logging():
    setup_logging()
    yield

# @pytest.fixture(scope="session")
# def driver_manager():
#     manager = WebDriverSingleton.get_instance()
#     yield manager
#     manager.quit()
#
# @pytest.fixture(scope="session")
# def driver(driver_manager):
#     return driver_manager.get_driver()

