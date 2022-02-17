from locators.email_page_locators import EmailPageLocators
from pages.base_page import BasePage


class EmailPage(BasePage):
    def check_new_message(self):
        new_message = self.find_element(EmailPageLocators.TITLE_TEXT_IN_LAST_INCOME_MESSAGE)
        return new_message

    def email_andrmy_is_displayed(self):
        result_email = self.find_element(EmailPageLocators.TEST_LETTER_LOCATOR_ANDRMY)
        return result_email

    def get_sender_in_last_message(self):
        last_sender = self.find_element(EmailPageLocators.SENDER_IN_LAST_MESSAGE)
        return last_sender

    def get_sender_in_pre_last_message(self):
        pre_last_sender = self.find_element(EmailPageLocators.SENDER_IN_PRE_LAST_MESSAGE)
        return pre_last_sender

    def open_last_send_message(self):
        send_msg_btn = self.find_element(EmailPageLocators.SENT_MESSAGES_LINK)
        send_msg_btn.click()
        recip_in_last_message = self.find_element(EmailPageLocators.TEST_LETTER_LOCATOR_MYTEST)
        return recip_in_last_message
