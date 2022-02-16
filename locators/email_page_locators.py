from selenium.webdriver.common.by import By


class EmailPageLocators:
    INCOMING_MESSAGES = (By.XPATH, "//*[@id=':4d']")
    LAST_INCOME_MESSAGE = (By.XPATH, "//*[@id=':2c']")
    TITLE_TEXT_IN_LAST_INCOME_MESSAGE = (By.XPATH, "//*[@id=':2i")
    SENT_MESSAGES_LINK = (By.CSS_SELECTOR, ".aHS-bnu > div:nth-child(2)")
    RECIPIENT_IN_LAST_SENT_MESSAGE = (By.XPATH, "//*[@id=':61']/span")
    LAST_SENT_MESSAGE = (By.XPATH, "//*[@id=':5y']")
    SENDER_IN_LAST_MESSAGE = (By.XPATH, "//*[@id=':2a']/span/span")
    SENDER_IN_PRE_LAST_MESSAGE = (By.XPATH, "//*[@id=':2n']/span/span")
    TEST_LETTER_LOCATOR_ANDRMY = (By.XPATH, "//td//div[2]//*[@email='andrmytest1@gmail.com']")
    TEST_LETTER_LOCATOR_MYTEST = (By.XPATH, "//td//div[2]//*[@email='mytestand1@gmail.com']")
