from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from api_data import ApiData
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.recovery_page import RecoveryPage
from starburger_api import StarburgerApi


class TestAccountCabinet:
    def test_account_cabinet_button_pass(self, driver, create_user):
        email = create_user.json()['user']['email']
        account_cabinet = RecoveryPage(driver)
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        account_cabinet.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                           ApiData.BODY_USER_REGISTRATION['password'])
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        account_cabinet.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        login = account_cabinet.wait_and_find_element(LoginPageLocators.LOGIN_TEXT)
        assert login.get_attribute('value') == email

    def test_order_history(self, driver, create_user):
        email = create_user.json()['user']['email']
        token = create_user.json()['accessToken']
        order_response = StarburgerApi.create_order(token, ApiData.DODY_CREATE_ORDER)
        account_cabinet = RecoveryPage(driver)
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.click_element(LoginPageLocators.EMAIL_TEXT_FIELD)
        account_cabinet.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        account_cabinet.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                           ApiData.BODY_USER_REGISTRATION['password'])
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        account_cabinet.click_element(LoginPageLocators.ORDER_HISTORY_BUTTON)
        assert 'Сегодня' in account_cabinet.wait_and_find_element(LoginPageLocators.DATE_ORDER).text

    def test_logout(self, driver, create_user):
        email = create_user.json()['user']['email']
        account_cabinet = RecoveryPage(driver)
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.click_element(LoginPageLocators.EMAIL_TEXT_FIELD)
        account_cabinet.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        account_cabinet.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                           ApiData.BODY_USER_REGISTRATION['password'])
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.click_element(LoginPageLocators.LOGOUT_BUTTON)
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)
        assert account_cabinet.wait_and_find_element(LoginPageLocators.ENTER_BUTTON)
