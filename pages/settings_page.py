from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class SettingsPageLocators:
    button_settings = (By.XPATH, '//li[@class="_listItem_oltwr_40"][12]')
    button_general = (By.XPATH, '//div[@class="_tab_oqim5_8"][1]')
    input_first_name = (By.XPATH, '//input[@placeholder="First Name"]')
    input_last_name = (By.XPATH, '//input[@placeholder="Last Name"]')
    button_save = (By.XPATH, '//button[@class="_button_variant_solid_1o11o_8 _button_size_regular_1o11o_68 _button_color_third_1o11o_52 _button_noIcons_1o11o_78 _button_1yf2h_8"][1]')
    input_email = (By.XPATH, '//input[@placeholder="Email"]')


class SettingsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def clear_first_name(self):
        return self.find(SettingsPageLocators.input_first_name).clear()

    def clear_last_name(self):
        return self.find(SettingsPageLocators.input_last_name).send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)

    def fill_first_name(self, string):
        return self.find(SettingsPageLocators.input_first_name).send_keys(string)

    def fill_last_name(self, string):
        return self.find(SettingsPageLocators.input_last_name).send_keys(string)

    def click_save_button(self):
        return self.find(SettingsPageLocators.button_save).click()

    def get_first_name(self):
        return self.find(SettingsPageLocators.input_first_name).get_attribute("value")

    def get_last_name(self):
        return self.find(SettingsPageLocators.input_last_name).get_attribute("value")

    def click_settings_button(self):
        return self.find(SettingsPageLocators.button_settings).click()

    def clear_email(self):
        self.find(SettingsPageLocators.input_email).send_keys(Keys.CONTROL, "a")
        self.find(SettingsPageLocators.input_email).send_keys(Keys.DELETE)

    def clear_email(self):
        return self.find(SettingsPageLocators.input_email).send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)

    def clear_email(self):
        return self.find(SettingsPageLocators.input_email).send_keys(Keys.BACKSPACE*20)

    def fill_email(self, string):
        return self.find(SettingsPageLocators.input_email).send_keys(string)

    def get_email(self):
        return self.find(SettingsPageLocators.input_email).get_attribute("value")
