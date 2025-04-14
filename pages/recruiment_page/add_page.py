from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.recruiment_page.vacancies_page import Vacancies


class AddPage(BasePage):
    #LOCATORS
    VACANCY_NAME = (By.XPATH,"(//input[contains(@class,'oxd-input')])[2]")
    DESCRIPTION = (By.XPATH,"//textarea[@placeholder='Type description here']")
    JOB_TITLE = (By.CLASS_NAME,"oxd-select-text--after")
    JOB_TITLE_OPTION = (By.XPATH,"//span[contains(text(),'job_title')]")
    HIRING_MANAGER = (By.XPATH,"//input[@placeholder='Type for hints...']")
    NUMBER_OF_POS = (By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div[2]/div/div/div/div[2]")
    ADD_BUTTON = (By.XPATH,"//button[@type='submit']")
    ADD_PAGE_TITLE = (By.XPATH,"//h6[text()='Add Vacancy']")
    HIRING_MANAGER_RESULT = (By.XPATH,"//div[@role='option']//span[text()='manager_name']")

    def __init__(self,driver):
        super().__init__(driver)

    def add_vacancy(self,**kwargs):
        """
        Please input text value for these parameters below to add a valid vacancy
        :param kwargs: 'name', 'job title', 'description', 'hiring manager', 'number'
        :return: Vacancies Page
        """
        self.enter_vancancy_name(kwargs['vacancy_name'])
        self.choose_job_title(kwargs['job_title'])
        self.enter_description(kwargs['description'])
        self.select_hiring_manager(kwargs['hiring_manager'])
        #self.enter_numberOfPos(kwargs['num_pos'])
        self.find_clickable_element(self.ADD_BUTTON).click()
        return Vacancies(self.driver)


    def enter_vancancy_name(self,name):
        vacancy_name_field = self.find_element(self.VACANCY_NAME)
        vacancy_name_field.send_keys(name)
        return self

    def enter_description(self,description=""):
        description_field = self.find_element(self.DESCRIPTION)
        description_field.send_keys(description)
        return self

    def choose_job_title(self,job_title=""):
        #Click Job Title
        self.find_clickable_element(self.JOB_TITLE).click()
        #Click Job title option
        job_title_cv2list = list(self.JOB_TITLE_OPTION)
        job_title_cv2list[1] = job_title_cv2list[1].replace("job_title",job_title)
        self.find_clickable_element(job_title_cv2list).click()
        return self

    def select_hiring_manager(self,hiring_manager=""):
        hiring_manager_option = self.find_element(self.HIRING_MANAGER)
        hiring_manager_option.send_keys(hiring_manager)
        hr_name = list(self.HIRING_MANAGER_RESULT)
        hr_name[1] = hr_name[1].replace("manager_name",hiring_manager)
        self.find_clickable_element(hr_name).click()
        return self

    def enter_numberOfPos(self,number=''):
        pos_num = self.find_element(self.NUMBER_OF_POS)
        pos_num.send_keys(number)
        return self

    def is_addpage_loaded(self):
        return self.element_is_present(self.ADD_PAGE_TITLE)







