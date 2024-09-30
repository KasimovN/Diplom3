from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.recovery_page_locators import RecoveryPageLocators
from pages.recovery_page import RecoveryPage


class TestRecoveryPassword:
    def test_load_recovery_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.click_element(MainPageLocators.ACCOUNT_BUTTON)
        recovery_page.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'

    def test_click_recovery_button(self, create_user, driver):
        email = create_user.json()['user']['email']
        recovery_button = RecoveryPage(driver)
        recovery_button.click_element(MainPageLocators.ACCOUNT_BUTTON)
        recovery_button.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)
        recovery_button.filling_text_field(RecoveryPageLocators.EMAIL_TEXT_FIELD, email)
        recovery_button.click_element(RecoveryPageLocators.RECOVERY_BUTTON)
        assert recovery_button.wait_and_find_element(RecoveryPageLocators.RECOVERY_BUTTON)

    def test_visible_password_field(self, create_user, driver):
        email = create_user.json()['user']['email']
        recovery_visible_button = RecoveryPage(driver)
        recovery_visible_button.click_element(MainPageLocators.ACCOUNT_BUTTON)
        recovery_visible_button.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)
        recovery_visible_button.filling_text_field(RecoveryPageLocators.EMAIL_TEXT_FIELD, email)
        recovery_visible_button.click_element(RecoveryPageLocators.RECOVERY_BUTTON)
        recovery_visible_button.wait_and_find_element(RecoveryPageLocators.VISIBLE_PASSWORD_BUTTON).click()
        password_field = recovery_visible_button.wait_and_find_element(RecoveryPageLocators.PASSWORD_TEXT_FIELD)
        assert password_field.get_attribute('type') == 'text'
