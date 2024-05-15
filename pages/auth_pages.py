from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthPageLocators:
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

    def cheat_login(self):
        self.browser.execute_script("window.localStorage.setItem('access', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiI2NDQ4MmJmZS05MmM1LTQwOGQtYjA1Yi03YzgwZjNhYzcxOTkiLCJpc3MiOiJjc3NfYXV0aCIsInN1YiI6IjYxMzdmMzAyLWMyNWEtNDVkMi1iOTc3LWQzZDEzMTI5ZjUyNyIsImp0aSI6ImQ4YzVhNWIwLWY2MjYtNDE3ZC05NDViLWRjNTA4ZGJlZGRmNSIsImlhdCI6MTcxMTQ1MDQ0NCwibmJmIjoxNzExNDUwNDQ0LCJ0eXBlIjoiYWNjZXNzIn0.996Q8IwF67xWhieNs1DUrHSMff3cXpu_HsT_Rmz9PL0');")
        self.browser.execute_script("window.localStorage.setItem('refresh', 'abc');")
        self.browser.get('https://test.chain-serve.com/dashboard')

    def email_button(self):
        return self.find(AuthPageLocators.button_email)

    def email_input(self):
        return self.find(AuthPageLocators.input_email)

    def fill_email(self, string):
        return self.find(AuthPageLocators.input_email).send_keys(string)

    def next_button(self):
        return self.find(AuthPageLocators.button_next)

    def fill_password(self, string):
        return self.find(AuthPageLocators.input_password).send_keys(string)

    def log_in_button(self):
        return self.find(AuthPageLocators.button_log_in)

