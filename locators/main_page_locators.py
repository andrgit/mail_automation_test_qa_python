from selenium.webdriver.common.by import By


class MainPageLocators:
    EMAIL_FIELD_LOCATOR = (By.XPATH, "//*[@id='identifierId']")
    NEXT_BTN_IN_EMAIL_LOCATOR = (By.XPATH, "//*[@id='identifierNext']")
    PASSWORD_FIELD_LOCATOR = (By.XPATH, "//*[@name='password']")
    NEXT_BTN_IN_PASSWORD_LOCATOR = (By.XPATH, "//*[@id='passwordNext']")
