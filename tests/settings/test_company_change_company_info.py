from pages.settings_company_page import SettingsPage
from pages.settings_company_page import SettingsPageLocators
from time import sleep
from utills.random_utills import generate_random_phone
from utills.random_utills import generate_random_company_name
from utills.random_utills import generate_random_alternate_name
from utills.random_utills import generate_random_month
from utills.random_utills import generate_random_day
from utills.random_utills import generate_random_year
from utills.random_utills import generate_random_website


def test_change_company_info(browser, open, sign_in_restaurant):
    settings = SettingsPage(browser)
    settings.find_element(SettingsPageLocators.button_settings).click()
    settings.find_element(SettingsPageLocators.button_company).click()
    settings.find_element(SettingsPageLocators.input_company_name).click()
    sleep(0.1)
    settings.clear_company_name()
    new_company_name = generate_random_company_name()
    settings.fill_company_name(new_company_name)
    settings.find_element(SettingsPageLocators.input_alternate_name).click()
    sleep(0.1)
    settings.clear_alternate_name()
    new_alternate_name = generate_random_alternate_name()
    settings.fill_alternate_name(new_alternate_name)
    settings.find_element(SettingsPageLocators.input_website).click()
    sleep(0.1)
    settings.clear_website()
    new_website = generate_random_website()
    settings.fill_website(new_website)
    old_date_founded = settings.get_date_founded()
    settings.find_element(SettingsPageLocators.month_founded).click()
    sleep(0.1)
    settings.clear_month_founded()
    new_month_founded = generate_random_month()
    settings.fill_month_founded(new_month_founded)
    settings.find_element(SettingsPageLocators.day_founded).click()
    sleep(0.1)
    settings.clear_day_founded()
    new_day_founded = generate_random_day()
    settings.fill_day_founded(new_day_founded)
    settings.find_element(SettingsPageLocators.year_founded).click()
    sleep(0.1)
    settings.clear_year_founded()
    new_year_founded = generate_random_year()
    settings.fill_year_founded(new_year_founded)
    settings.find_element(SettingsPageLocators.input_phone).click()
    sleep(0.1)
    settings.clear_phone()
    new_phone = generate_random_phone()
    settings.fill_phone(new_phone)
    settings.find_element(SettingsPageLocators.save_button).click()
    company_name = settings.get_company_name()
    alternate_name = settings.get_alternate_name()
    website = settings.get_website()
    date_founded = settings.get_date_founded()
    phone = settings.get_phone()
    assert new_company_name == company_name
    assert new_alternate_name == alternate_name
    assert new_website == website
    assert old_date_founded != date_founded
    assert new_phone == phone