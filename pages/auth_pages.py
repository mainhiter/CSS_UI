from pages.base_page import BasePage
from selenium.webdriver.common.by import By



button_email = (By.XPATH, '//button[@class="_button_default_octaa_21 _button_default_selected_octaa_54"]')
input_email = (By.XPATH, '//input[@class="_input_1w6ft_33"]')
button_next = (By.XPATH, '//button[@class="_button_variant_solid_1o11o_8 _button_size_regular_1o11o_68 _button_color_second_1o11o_46 _button_noIcons_1o11o_78"]')
input_password = (By.XPATH, '//input[@class="_input_1w6ft_33 _input_endIcon_1w6ft_75"]')
button_log_in = (By.XPATH, '//button[@class="_button_variant_solid_1o11o_8 _button_size_regular_1o11o_68 _button_color_second_1o11o_46 _button_noIcons_1o11o_78"]')


class SignInPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://test.chain-serve.com/auth')

    # def open2(self):
    #     self.browser.get('https://test.chain-serve.com/registration')

    def email_button(self):
        return self.find(button_email)

    def email_input(self):
        return self.find(input_email)

    def fill_email(self, string):
        return self.find(input_email).send_keys(string)

    def next_button(self):
        return self.find(button_next)

    def fill_password(self, string):
        return self.find(input_password).send_keys(string)

    def log_in_button(self):
        return self.find(button_log_in)

