from pages.base_page import BasePage


class TestVacancies(BasePage):
    @classmethod
    def setUpClass(cls):
        from utils.driver_manager import WebDriverSingleton
        cls.driver_manager = WebDriverSingleton.get_instance()
        cls.driver = cls.driver_manager.driver
        cls.vacancies_page =