from pages.dashboard_page import DashboardPageLocators
from pages.dashboard_page import DashboardPage
from time import sleep

def test_sign_in(browser, open, sign_in_cheat):
    dashboard = DashboardPage(browser)
    dashboard_button_text = dashboard.find(DashboardPageLocators.button_dashboard).text
    assert 'Dashboard' in dashboard_button_text













    # sign_in_page = SignInPage(browser)
    # sign_in_page.open()
    # sign_in_page.cheat_login()
    # sleep(2)