from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Recruitment(BasePage):
    #LOCATORS
    RECRUITMENT_PAGE = (By.XPATH,"//h6[text()='Recruitment']")
    CONTAINS_OPTION = (By.XPATH,"//span[contains(text(),'{select_option}')]")
    VACANCIES_TAB = (By.CSS_SELECTOR,"li[class='oxd-topbar-body-nav-tab'] a[class='oxd-topbar-body-nav-tab-item']")


    def is_recruitment_page_loaded(self):
        return self.element_is_present(self.RECRUITMENT_PAGE)

    def click_on_vacancies(self):
        self.find_clickable_element(self.VACANCIES_TAB).click()


    def select_dropdown_option(self, locator,option_text):
        super().click_dropdown(locator)
        option_selected = self.find_clickable_option(option_text)
        option_selected.click()

    def find_clickable_option(self,option_text):
        return self.wait.until().EC.element_to_be_clickable(f"//span[contains(text(),'{option_text}')]")



    def __init__(self, driver):
        super().__init__(driver)