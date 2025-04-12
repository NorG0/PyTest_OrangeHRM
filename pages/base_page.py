from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.decorator import handle_exception


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def openurl(self):
        if self.url:
            self.driver.get(self.url)
            self.wait.until(EC.presence_of_element_located(locator=(By.TAG_NAME, "h5")))
        else:
            raise Exception("URL is not defined")

    @handle_exception
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @handle_exception
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @handle_exception
    def element_is_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @handle_exception
    def click_dropdown(self, locator):
        self.find_element(locator).click()
        return self






