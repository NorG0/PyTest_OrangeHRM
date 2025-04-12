from selenium.webdriver.common.by import By
from utils.decorator import log_step, handle_exception
from pages import admin_page
from pages.base_page import BasePage
from pages.recruiment_page.recruitment_page import Recruitment


class DashboardPage(BasePage):
    #LOCATORS
    DASHBOARD_LAYOUT = (By.XPATH,"//div[contains(@class,'oxd-layout')]")
    PROFILE = (By.XPATH,"//li[@class='oxd-userdropdown']")
    MENU_ITEMS = (By.XPATH, "//span[contains(@class,'oxd-text oxd-text--span oxd-main-menu-item--name') and text()='item_text']")
    SIGN_OUT = (By.XPATH,"//a[contains(@class,'oxd-userdropdown-link') and text()='Logout']")

    MENU_ITEMS_CLASSES = {
        "Admin": admin_page,
        "recruitment": Recruitment

    }



    def __init__(self, driver):
        super().__init__(driver)


    def is_dashboard_page_loaded(self):
        return self.element_is_present(self.DASHBOARD_LAYOUT)

    @log_step
    @handle_exception
    def click_menu_item(self,item_text):
        locator = list(self.MENU_ITEMS)
        locator[1] = locator[1].replace("item_text",item_text)
        self.find_clickable_element(locator)
        key = item_text.lower()
        return self.MENU_ITEMS_CLASSES[key](self.driver)

    def dashboard_signout(self):
        from pages.login_page import LoginPage
        self.find_clickable_element(self.PROFILE).click()
        self.find_clickable_element(self.SIGN_OUT).click()
        return LoginPage(self.driver)





