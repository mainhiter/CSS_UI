from pages.auth_pages import SignInPage
from time import sleep

def test_sign_in(browser):
    sign_in_page = SignInPage(browser)
    sign_in_page.open()
    sleep(5)
    sign_in_page.email_input().click()
    sign_in_page.fill_email("appleid.hit@yandex.ru")
    sign_in_page.next_button().click()
    sleep(2)
    sign_in_page.fill_password("!Kolyapass1")
    sleep(2)
    sign_in_page.log_in_button().click()
    sleep(3)


    # sign_in_page2 = SignInPage(browser)
    # sign_in_page2.open2()
    # sleep(5)