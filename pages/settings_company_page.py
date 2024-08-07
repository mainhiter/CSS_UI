from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class SettingsPageLocators:
    button_settings = (By.XPATH, '//li[@class="_listItem_rf16o_41"][8]')
    button_company = (By.XPATH, '//div[@class="_tab_ci8vu_8"][2]')
    save_button = (By.XPATH, '//button[@class="_button_variant_solid_1o11o_8 _button_size_regular_1o11o_68 _button_color_third_1o11o_52 _button_noIcons_1o11o_78 _button_17sdb_8"]')
    input_company_name = (By.XPATH, '//input[@placeholder="Company Name"]')
    input_alternate_name = (By.XPATH, '//input[@placeholder="Alternate/DBA name"]')
    input_website = (By.XPATH, '//input[@placeholder="Website"]')
    month_founded = (By.XPATH, '//div[@class="_dateSegment_1p90k_103"][1]')
    day_founded = (By.XPATH, '//div[@class="_dateSegment_1p90k_103"][3]')
    year_founded = (By.XPATH, '//div[@class="_dateSegment_1p90k_103"][5]')
    input_phone = (By.XPATH, '//input[@placeholder="(123) 456-7890"]')
    all_date_founded = (By.XPATH, '//input[@class="react-aria-Input"][1]')
    button_sun = (By.XPATH, '//button[@class="_toggleButton_12ya4_28"][1]')
    button_mon = (By.XPATH, '//button[@class="_toggleButton_12ya4_28"][2]')
    button_tue = (By.XPATH, '//button[@class="_toggleButton_12ya4_28"][3]')
    button_wed = (By.XPATH, '//button[@class="_toggleButton_12ya4_28"][4]')
    button_thu = (By.XPATH, '//button[@class="_toggleButton_12ya4_28"][5]')
    button_fri = (By.XPATH, '//button[@class="_toggleButton_12ya4_28"][6]')
    button_sat = (By.XPATH, '//button[@class="_toggleButton_12ya4_28"][7]')
    opening_hour = (By.XPATH, '//div[@aria-label="hour, Opening time"]')
    closing_hour = (By.XPATH, '//div[@aria-label="hour, Closing time"]')
    opening_time = (By.XPATH, '//input[(@value="08:00:00") or (@value="09:00:00")]')
    closing_time = (By.XPATH, '//input[(@value="17:00:00") or (@value="18:00:00")]')




class SettingsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def clear_company_name(self):
        return self.find_element(SettingsPageLocators.input_company_name).clear()

    def fill_company_name(self, string):
        return self.find_element(SettingsPageLocators.input_company_name).send_keys(string)

    def clear_alternate_name(self):
        return self.find_element(SettingsPageLocators.input_alternate_name).clear()

    def fill_alternate_name(self, string):
        return self.find_element(SettingsPageLocators.input_alternate_name).send_keys(string)

    def clear_website(self):
        return self.find_element(SettingsPageLocators.input_website).clear()

    def fill_website(self, string):
        return self.find_element(SettingsPageLocators.input_website).send_keys(string)

    def clear_month_founded(self):
        return self.find_element(SettingsPageLocators.month_founded).clear()

    def clear_day_founded(self):
        return self.find_element(SettingsPageLocators.day_founded).clear()

    def clear_year_founded(self):
        return self.find_element(SettingsPageLocators.year_founded).clear()

    def fill_month_founded(self, string):
        return self.find_element(SettingsPageLocators.month_founded).send_keys(string)

    def fill_day_founded(self, string):
        return self.find_element(SettingsPageLocators.day_founded).send_keys(string)

    def fill_year_founded(self, string):
        return self.find_element(SettingsPageLocators.year_founded).send_keys(string)

    def clear_phone(self):
        return self.find_element(SettingsPageLocators.input_phone).clear()

    def fill_phone(self, string):
        return self.find_element(SettingsPageLocators.input_phone).send_keys(string)

    def get_company_name(self):
        return self.find_element(SettingsPageLocators.input_company_name).get_attribute("value")

    def get_alternate_name(self):
        return self.find_element(SettingsPageLocators.input_alternate_name).get_attribute("value")

    def get_website(self):
        return self.find_element(SettingsPageLocators.input_website).get_attribute("value")

    def get_date_founded(self):
        return self.find_element(SettingsPageLocators.all_date_founded).get_attribute("value")

    def get_phone(self):
        return self.find_element(SettingsPageLocators.input_phone).get_attribute("value")

    def get_all_date_founded(self):
        return self.find_element(SettingsPageLocators.all_date_founded).get_attribute("value")

    def click_day_sun(self):
        return self.find_element(SettingsPageLocators.button_sun).click()

    def click_day_mon(self):
        return self.find_element(SettingsPageLocators.button_mon).click()

    def click_day_tue(self):
        return self.find_element(SettingsPageLocators.button_tue).click()

    def click_day_wed(self):
        return self.find_element(SettingsPageLocators.button_wed).click()

    def click_day_thu(self):
        return self.find_element(SettingsPageLocators.button_thu).click()

    def click_day_fri(self):
        return self.find_element(SettingsPageLocators.button_fri).click()

    def click_day_sat(self):
        return self.find_element(SettingsPageLocators.button_sat).click()

    def get_day_sun_status(self):
        return self.find_element(SettingsPageLocators.button_sun).get_attribute("aria-pressed")

    def get_day_mon_status(self):
        return self.find_element(SettingsPageLocators.button_mon).get_attribute("aria-pressed")

    def get_day_tue_status(self):
        return self.find_element(SettingsPageLocators.button_tue).get_attribute("aria-pressed")

    def get_day_wed_status(self):
        return self.find_element(SettingsPageLocators.button_wed).get_attribute("aria-pressed")

    def get_day_thu_status(self):
        return self.find_element(SettingsPageLocators.button_thu).get_attribute("aria-pressed")

    def get_day_fri_status(self):
        return self.find_element(SettingsPageLocators.button_fri).get_attribute("aria-pressed")

    def get_day_sat_status(self):
        return self.find_element(SettingsPageLocators.button_sat).get_attribute("aria-pressed")

    def click_opening_hour(self):
        return self.find_element(SettingsPageLocators.opening_hour).click()

    def fill_opening_hour(self, integer):
        return self.find_element(SettingsPageLocators.opening_hour).send_keys(integer)

    def click_closing_hour(self):
        return self.find_element(SettingsPageLocators.closing_hour).click()

    def fill_closing_hour(self, integer):
        return self.find_element(SettingsPageLocators.closing_hour).send_keys(integer)

    def get_opening_time(self):
        return self.find_element(SettingsPageLocators.opening_time).get_attribute("value")

    def get_closing_time(self):
        return self.find_element(SettingsPageLocators.closing_time).get_attribute("value")
