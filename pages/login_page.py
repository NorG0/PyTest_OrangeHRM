
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from utils.decorator import handle_exception, log_step


class LoginPage(BasePage):
    # Locators as class variables
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    USERNAME_FAILED_MSG = (By.XPATH,"(//span[contains(@class,'oxd-input-field-error-message') and text()='Required'])[1]")
    PASSWORD_FAILED_MSG = (By.XPATH,"(//span[contains(@class,'oxd-input-field-error-message') and text()='Required'])[2]")


    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return DashboardPage(self.driver)

    @log_step
    def enter_username(self, username):
        us_filed = self.driver.find_element(*self.USERNAME_INPUT)
        us_filed.clear()
        us_filed.send_keys(username)
        return self

    @log_step
    def enter_password(self, password):
        pw_field = self.driver.find_element(*self.PASSWORD_INPUT)
        pw_field.clear()
        pw_field.send_keys(password)
        return self

    @log_step
    def click_login(self):
        self.find_clickable_element(self.LOGIN_BUTTON).click()
        return self

    @handle_exception
    def is_login_page_loaded(self):
        return self.element_is_present(self.LOGIN_BUTTON)

    @handle_exception
    def is_error_msg_displayed(self):
        return self.element_is_present(self.ERROR_MESSAGE)

    def get_error_msg(self):
        if self.is_error_msg_displayed():
            return self.find_element(self.ERROR_MESSAGE).text

    def is_username_error_msg_displayed(self):
        return self.find_element(self.USERNAME_FAILED_MSG)

    def get_username_error_msg(self):
        if self.is_username_error_msg_displayed():
            return self.find_element(self.USERNAME_FAILED_MSG).text

    def is_password_error_msg_displayed(self):
        return self.find_element(self.PASSWORD_FAILED_MSG)

    def get_password_error_msg(self):
        if self.is_password_error_msg_displayed():
            return self.find_element(self.PASSWORD_FAILED_MSG).text








