from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DashboardPageLocators:
    button_dashboard = (By.XPATH, '//li[@class="_listItem_oltwr_40"][1]')


class DashboardPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_dashboard_button(self):
        return self.find(DashboardPageLocators.button_dashboard).click()