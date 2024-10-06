from locators.recovery_page_locators import RecoveryPageLocators
from pages.login_page import LoginPage


class RecoveryPage(LoginPage):
    def recovery_page_fill_email(self, email):
        self.filling_text_field(RecoveryPageLocators.EMAIL_TEXT_FIELD, email)

    def recovery_page_click_recovery_button(self):
        self.click_element(RecoveryPageLocators.RECOVERY_BUTTON)

    def recovery_page_password_text_field(self):
        return self.wait_and_find_element(RecoveryPageLocators.PASSWORD_TEXT_FIELD)

    def recovery_page_click_visible_password(self):
        self.click_element(RecoveryPageLocators.VISIBLE_PASSWORD_BUTTON)
