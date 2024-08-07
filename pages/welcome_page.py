from pages.base_page import BasePage
from selenium.webdriver.common.by import By


input_password = (By.XPATH, '//input[@class="_input_1w6ft_33 _input_endIcon_1w6ft_75"]')

class WelcomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def fill_password(self, string):
        return self.find_element(input_password).send_keys(string)

