import unittest

from pages.dashboard_page import DashboardPage


class TestRecruitment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from utils.driver_manager import WebDriverSingleton
        cls.driver_manager = WebDriverSingleton.get_instance()
        cls.driver = cls.driver_manager.driver
        cls.dashboard_page = DashboardPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        from pages.login_page import LoginPage
        self.dashboard_page.openurl()
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login("Admin", "admin123").is_dashboard_page_loaded()

    def test_click_recruitment(self):
        recruitment_page = self.dashboard_page.click_menu_item("Recruitment")
        self.assertTrue(recruitment_page.is_recruitment_page_loaded(),"No Recruitment Page Found")



if __name__ == "__main__":
    unittest.main()






