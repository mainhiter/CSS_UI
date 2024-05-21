import pytest
from pages.settings_page import SettingsPage
from pages.settings_page import SettingsPageLocators
from pages.dashboard_page import DashboardPage
from time import sleep
from utills.random_utills import generate_random_email


@pytest.mark.actual
def test_change_email(browser, open, sign_in_cheat):
    sleep(2)
    settings = SettingsPage(browser)
    dashboard = DashboardPage(browser)
    settings.click_settings_button()
    settings.find(SettingsPageLocators.input_email).click()
    sleep(1)
    settings.clear_email()
    sleep(5)
    # email = generate_random_email()
    # settings.fill_email(email)
    # sleep(3)
    # settings.click_save_button()
    # sleep(2)
    # dashboard.click_dashboard_button()
    # sleep(3)
    # settings.click_settings_button()
    # sleep(3)
    # assert email == settings.get_email()
