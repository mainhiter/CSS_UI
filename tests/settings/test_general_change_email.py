import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.settings_general_page import SettingsPage
from pages.settings_general_page import SettingsPageLocators
from pages.dashboard_page import DashboardPage
from time import sleep
from utills.random_utills import generate_random_email
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_change_email(browser, open, sign_in_restaurant):
    settings = SettingsPage(browser)
    settings.click_settings_button()
    settings.find_element(SettingsPageLocators.input_email).click()
    # WebDriverWait(browser, 10).until(
    # EC.text_to_be_present_in_element_attribute((By.XPATH, '//input[@placeholder="Email"]'), 'data-focused', 'true')
    # )
    sleep(0.1)  # без слипа никак не работает, даже вэйтер выше не помогает
    settings.clear_email()
    email = generate_random_email()
    settings.fill_email(email)
    settings.click_save_button()
    new_email = settings.get_email()
    assert email == new_email
