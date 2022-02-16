import allure

from pages.main_page import MainPage


@allure.story("Send and check send message")
def test_send_and_check_last_send_message(driver, send_new_message):
    """
    The test send new message from andrmytest1@gmail.com and check send message
    recipient mytestand1@gmail.com
    """
    email_andrmy = 'andrmytest1@gmail.com'
    password_andrmy = 'password123@'
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open email page and send mail data'):
        email_page = page.open_email_page(email_andrmy, password_andrmy)
    with allure.step('Check In email page,the necessary email in the send messages'):
        last_send_message = email_page.open_last_send_message()
    assert "mytestand1" in last_send_message.text, "We have a problem"


@allure.story("Send and check income message in gmail2")
def test_check_last_get_message(driver):
    """
    The test open gmail link and check income message
    """
    email_mytest = 'mytestand1@gmail.com'
    password_mytest = 'password123@'
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open email page and send mail data'):
        email_page = page.open_email_page(email_mytest, password_mytest)
    with allure.step('Check In email page,the necessary email in incoming messages'):
        get_email = email_page.email_andrmy_is_displayed()
    assert get_email.is_displayed(), "We have a problem"
