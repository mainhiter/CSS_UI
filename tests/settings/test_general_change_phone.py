import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.settings_general_page import SettingsPage
from pages.settings_general_page import SettingsPageLocators
from pages.dashboard_page import DashboardPage
from time import sleep
from utills.random_utills import generate_random_phone
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_change_phone(browser, open, sign_in_restaurant):
    settings = SettingsPage(browser)
    settings.click_settings_button()
    settings.find_element(SettingsPageLocators.input_phone).click()
    sleep(0.1)
    settings.clear_phone()
    phone = generate_random_phone()
    settings.fill_phone(phone)
    settings.click_save_button()
    new_phone = settings.get_phone()
    assert phone == new_phone

