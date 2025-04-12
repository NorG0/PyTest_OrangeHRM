
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



# Interface for WebDriver Manager
class IWebDriverManager(ABC):
    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def quit(self):
        pass


# Singleton Pattern for WebDriver
class WebDriverSingleton(IWebDriverManager):
    _instance = None

    @staticmethod
    def get_instance():
        if WebDriverSingleton._instance is None:
            WebDriverSingleton()
        return WebDriverSingleton._instance

    def __init__(self):
        if WebDriverSingleton._instance is not None:
            raise Exception("WebDriverSingleton is a singleton class!")
        else:
            service = Service(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            # Add any Chrome options here
            # options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=service, options=options)
            self.driver.maximize_window()
            WebDriverSingleton._instance = self

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
            WebDriverSingleton._instance = None

