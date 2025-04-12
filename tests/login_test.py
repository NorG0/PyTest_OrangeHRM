import unittest

from pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from utils.driver_manager import WebDriverSingleton
        cls.driver_manager = WebDriverSingleton.get_instance()
        cls.driver = cls.driver_manager.driver
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def setUp(self):
        self.login_page.openurl()

    def test_login_valid(self):
        dashboard_page = self.login_page.login("Admin", "admin123")
        self.assertTrue(dashboard_page.is_dashboard_page_loaded(),"No Dashboard Page Found")
        #Sign Out
        login_page = dashboard_page.dashboard_signout()
        self.assertTrue(login_page.is_login_page_loaded(),"No Login Page Found")


    def test_login_invalid(self):
        self.login_page.login("Admin", "admin1234")
        #Check error msg
        self.assertTrue(self.login_page.is_error_msg_displayed(),"Error msg not displayed")
        self.assertEqual(self.login_page.get_error_msg(),"Invalid credentials")

    def test_login_empty(self):
        self.login_page.login(username="",password="")
        #Check input error msg
        self.assertEqual(self.login_page.get_username_error_msg(),"Required")
        self.assertEqual(self.login_page.get_password_error_msg(),"Required")


if __name__ == "__main__":
    unittest.main()

