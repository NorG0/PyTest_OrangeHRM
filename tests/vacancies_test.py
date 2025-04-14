import unittest

from pages.recruiment_page.vacancies_page import Vacancies
from utils.decorator import log_step, handle_exception


class TestVacancies(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from utils.driver_manager import WebDriverSingleton
        cls.driver_manager = WebDriverSingleton.get_instance()
        cls.driver = cls.driver_manager.driver
        cls.vacancies_page = Vacancies(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        from pages.login_page import LoginPage
        self.vacancies_page.openurl()
        self.loginPage = LoginPage(self.driver)
        dashboard = self.loginPage.login("Admin", "admin123")
        vacancies_page = dashboard.click_menu_item("Recruitment").click_on_vacancies()
        self.assertTrue(vacancies_page.is_vacancies_page_loaded(),"NO VACANCIES PAGE FOUND")

    def test_add_valid_vacancy(self):
        add_page = self.vacancies_page.click_add_button()
        self.assertTrue(add_page.is_addpage_loaded(),"No ADD PAGE FOUND")
        add_page.add_vacancy(vacancy_name='Automation Tester Mid',
                             job_title='QA Engineer', hiring_manager='Rahul Mulge Patil',
                             description='3 Years in testing software')






