import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.settings_general_page import SettingsPage
from pages.settings_general_page import SettingsPageLocators
from pages.dashboard_page import DashboardPage
from utills.random_utills import generate_random_first_name
from utills.random_utills import generate_random_last_name
from time import sleep


def test_change_first_and_last_names(browser, open, sign_in_restaurant):
    settings = SettingsPage(browser)
    settings.click_settings_button()
    settings.find_element(SettingsPageLocators.input_first_name).click()
    # WebDriverWait(browser, 10).until(
    # EC.text_to_be_present_in_element_attribute((By.XPATH, '//input[@placeholder="First Name"]'), 'data-focused', 'true')
    # )
    sleep(0.1) # без слипа никак не работает, даже вэйтер выше не помогает
    settings.clear_first_name()
    first_name = generate_random_first_name()
    settings.fill_first_name(first_name)
    settings.clear_last_name()
    last_name = generate_random_last_name()
    settings.fill_last_name(last_name)
    settings.click_save_button()
    new_first_name = settings.get_first_name()
    new_last_name = settings.get_last_name()
    assert first_name == new_first_name
    assert last_name == new_last_name
