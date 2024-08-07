from pages.settings_company_page import SettingsPage
from pages.settings_company_page import SettingsPageLocators
from time import sleep


def test_change_hours_of_operation(browser, open, sign_in_restaurant):
    settings = SettingsPage(browser)
    settings.find_element(SettingsPageLocators.button_settings).click()
    settings.find_element(SettingsPageLocators.button_company).click()
    sun_status = settings.get_day_sun_status()
    mon_status = settings.get_day_mon_status()
    tue_status = settings.get_day_tue_status()
    wed_status = settings.get_day_wed_status()
    thu_status = settings.get_day_thu_status()
    fri_status = settings.get_day_fri_status()
    sat_status = settings.get_day_sat_status()
    settings.click_day_sun()
    settings.click_day_mon()
    # aaa = settings.get_day_mon_status() идут ошибки потому что оно не успевает нормально прокликать
    settings.click_day_tue()
    settings.click_day_wed()
    settings.click_day_thu()
    settings.click_day_fri()
    settings.click_day_sat()
    opening_time = settings.get_opening_time()
    if opening_time == '08:00:00':
        settings.fill_opening_hour(9)
    else:
        settings.fill_opening_hour(8)
    settings.click_closing_hour()
    closing_time = settings.get_closing_time()
    if closing_time == '17:00:00':
        settings.fill_closing_hour(6)
    else:
        settings.fill_closing_hour(5)
    settings.find_element(SettingsPageLocators.save_button).click()
    new_sun_status = settings.get_day_sun_status()
    new_mon_status = settings.get_day_mon_status()
    new_tue_status = settings.get_day_tue_status()
    new_wed_status = settings.get_day_wed_status()
    new_thu_status = settings.get_day_thu_status()
    new_fri_status = settings.get_day_fri_status()
    new_sat_status = settings.get_day_sat_status()
    new_opening_time = settings.get_opening_time()
    new_closing_time = settings.get_closing_time()
    assert new_sun_status != sun_status
    assert new_mon_status != mon_status
    assert new_tue_status != tue_status
    assert new_wed_status != wed_status
    assert new_thu_status != thu_status
    assert new_fri_status != fri_status
    assert new_sat_status != sat_status
    assert new_opening_time != opening_time
    assert new_closing_time != closing_time








