from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class Vacancies(BasePage):
    #LOCATORS
    VACANCIES_TITLE = (By.XPATH,"//h5[text()='Vacancies']")
    ADD_BUTTON = (By.XPATH,"//html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")


    def __init__(self,driver):
        super().__init__(driver)


    def click_add_button(self):
        from pages.recruiment_page.add_page import AddPage
        self.find_clickable_element(self.ADD_BUTTON).click()
        return AddPage(self.driver)

    def is_vacancies_page_loaded(self):
        return self.element_is_present(self.VACANCIES_TITLE)






