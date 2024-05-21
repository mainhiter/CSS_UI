import pytest

from pages.settings_page import SettingsPage
from pages.settings_page import SettingsPageLocators
from pages.dashboard_page import DashboardPage
from utills.random_utills import generate_random_first_name
from utills.random_utills import generate_random_last_name
from time import sleep


def test_change_first_and_last_names(browser, open, sign_in_cheat):
    sleep(2)
    settings = SettingsPage(browser)
    dashboard = DashboardPage(browser)
    settings.click_settings_button()
    settings.find(SettingsPageLocators.input_first_name).click()
    settings.clear_first_name()
    sleep(5)
    first_name = generate_random_first_name()
    settings.fill_first_name(first_name)
    sleep(5)
    settings.clear_last_name()
    sleep(5)
    last_name = generate_random_last_name()
    settings.fill_last_name(last_name)
    sleep(5)
    settings.click_save_button()
    sleep(2)
    dashboard.click_dashboard_button()
    sleep(3)
    settings.click_settings_button()
    sleep(5)
    assert first_name != settings.get_first_name()
    assert last_name == settings.get_last_name()
