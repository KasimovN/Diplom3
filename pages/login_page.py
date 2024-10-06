from locators.login_page_locators import LoginPageLocators
from pages.main_page import MainPage


class LoginPage(MainPage):
    def login_page_title(self):
        return self.wait_and_find_element(LoginPageLocators.TITLE)
    def login_page_fill_password(self, password):
        self.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD, password)

    def login_page_fill_email(self, mail):
        self.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, mail)

    def login_page_log_in(self):
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    def login_page_login_text(self):
        return self.wait_and_find_element(LoginPageLocators.LOGIN_TEXT)

    def login_page_click_order_history(self):
        self.click_element(LoginPageLocators.ORDER_HISTORY_BUTTON)

    def login_page_click_logout(self):
        self.click_element(LoginPageLocators.LOGOUT_BUTTON)

    def login_page_click_recovery_button(self):
        self.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)
