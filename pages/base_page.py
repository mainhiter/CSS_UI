from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator):
        return WebDriverWait(
            self.browser,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[StaleElementReferenceException, TimeoutException],
        ).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )







