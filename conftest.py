from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser
@pytest.fixture()
def open(browser):
    browser.get('https://test.chain-serve.com/auth')

@pytest.fixture()
def sign_in_cheat(browser):
    browser.execute_script("window.localStorage.setItem('access', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiI2NDQ4MmJmZS05MmM1LTQwOGQtYjA1Yi03YzgwZjNhYzcxOTkiLCJpc3MiOiJjc3NfYXV0aCIsInN1YiI6IjYxMzdmMzAyLWMyNWEtNDVkMi1iOTc3LWQzZDEzMTI5ZjUyNyIsImp0aSI6ImQ4YzVhNWIwLWY2MjYtNDE3ZC05NDViLWRjNTA4ZGJlZGRmNSIsImlhdCI6MTcxMTQ1MDQ0NCwibmJmIjoxNzExNDUwNDQ0LCJ0eXBlIjoiYWNjZXNzIn0.996Q8IwF67xWhieNs1DUrHSMff3cXpu_HsT_Rmz9PL0');")
    browser.execute_script("window.localStorage.setItem('refresh', 'abc');")
    browser.get('https://test.chain-serve.com/dashboard')
