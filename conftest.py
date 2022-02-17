import pytest
import yagmail
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def send_new_message():
    mymail = 'andrmytest1@gmail.com'
    mail_password = 'password123@'

    yag = yagmail.SMTP(mymail, mail_password)
    contents = [
        "This is the letter, and here test text."
    ]

    return yag.send('mytestand1@gmail.com', 'Test Letter', contents)
