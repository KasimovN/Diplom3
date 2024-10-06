from data import StarBurgerData
from pages.recovery_page import RecoveryPage


class TestRecoveryPassword:
    def test_load_recovery_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.main_page_click_to_login()
        recovery_page.login_page_click_recovery_button()
        assert driver.current_url == StarBurgerData.FORGOT_PASSWORD_URL

    def test_click_recovery_button(self, create_user, driver):
        email = create_user.json()['user']['email']
        recovery_button = RecoveryPage(driver)
        recovery_button.main_page_click_to_login()
        recovery_button.login_page_click_recovery_button()
        recovery_button.recovery_page_fill_email(email)
        recovery_button.recovery_page_click_recovery_button()
        assert recovery_button.recovery_page_password_text_field()

    def test_visible_password_field(self, create_user, driver):
        email = create_user.json()['user']['email']
        recovery_visible_button = RecoveryPage(driver)
        recovery_visible_button.main_page_click_to_login()
        recovery_visible_button.login_page_click_recovery_button()
        recovery_visible_button.recovery_page_fill_email(email)
        recovery_visible_button.recovery_page_click_recovery_button()
        recovery_visible_button.recovery_page_click_visible_password()
        password_field = recovery_visible_button.recovery_page_password_text_field().get_attribute('type')
        assert password_field == 'text'
