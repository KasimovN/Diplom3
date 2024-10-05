from api_data import ApiData
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.recovery_page import RecoveryPage
from starburger_api import StarburgerApi


class TestAccountCabinet:
    def test_account_cabinet_button_pass(self, driver, create_user):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        account_cabinet = RecoveryPage(driver)
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)  # Переходим на странциу "Личный кабинет"
        account_cabinet.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        account_cabinet.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                           ApiData.BODY_USER_REGISTRATION['password'])
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)  # Авторизовываемся
        account_cabinet.wait_close_modal_page()
        account_cabinet.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)  # Ожидаем прогрузки страницы
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)  # Переходим в личный кабинет
        login = account_cabinet.wait_and_find_element(LoginPageLocators.LOGIN_TEXT)
        assert login.get_attribute('value') == email

    def test_order_history(self, driver, create_user):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        token = create_user.json()['accessToken']  # Запоминаем токен временного пользователя
        order_response = StarburgerApi.create_order(token, ApiData.DODY_CREATE_ORDER)  # Создаем заказ через API
        account_cabinet = RecoveryPage(driver)
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.click_element(LoginPageLocators.EMAIL_TEXT_FIELD)
        account_cabinet.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        account_cabinet.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                           ApiData.BODY_USER_REGISTRATION['password'])
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)  # Авторизовываемся
        account_cabinet.wait_close_modal_page()
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.wait_close_modal_page()
        account_cabinet.click_element(LoginPageLocators.ORDER_HISTORY_BUTTON)  # Заходим в историю заказов
        assert account_cabinet.wait_and_find_element(LoginPageLocators.DATE_ORDER).text

    def test_logout(self, driver, create_user):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        account_cabinet = RecoveryPage(driver)
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.click_element(LoginPageLocators.EMAIL_TEXT_FIELD)
        account_cabinet.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        account_cabinet.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                           ApiData.BODY_USER_REGISTRATION['password'])
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)  # Авторизовываемся
        account_cabinet.wait_close_modal_page()
        account_cabinet.click_element(MainPageLocators.ACCOUNT_BUTTON)
        account_cabinet.click_element(LoginPageLocators.LOGOUT_BUTTON)
        account_cabinet.wait_close_modal_page()
        account_cabinet.click_element(LoginPageLocators.ENTER_BUTTON)  # Выход из личного кабинета
        assert account_cabinet.wait_and_find_element(LoginPageLocators.ENTER_BUTTON)
