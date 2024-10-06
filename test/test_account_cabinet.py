from api_data import ApiData
from pages.login_page import LoginPage
from pages.order_list import OrderListPage
from starburger_api import StarburgerApi


class TestAccountCabinet:
    def test_account_cabinet_button_pass(self, driver, create_user):
        email = create_user.json()['user']['email']
        account_cabinet = LoginPage(driver)
        account_cabinet.main_page_click_to_login()
        account_cabinet.login_page_fill_email(email)
        account_cabinet.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        account_cabinet.login_page_log_in()
        account_cabinet.wait_close_modal_page()
        account_cabinet.main_page_wait_and_find_kraternaya_bulka()
        account_cabinet.main_page_click_to_login()
        login = account_cabinet.login_page_login_text()
        assert login.get_attribute('value') == email

    def test_order_history(self, driver, create_user):
        email = create_user.json()['user']['email']
        token = create_user.json()['accessToken']
        order_response = StarburgerApi.create_order(token, ApiData.DODY_CREATE_ORDER)
        order_history = OrderListPage(driver)
        order_history.main_page_click_to_login()
        order_history.login_page_fill_email(email)
        order_history.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        order_history.login_page_log_in()
        order_history.wait_close_modal_page()
        order_history.main_page_click_to_login()
        order_history.wait_close_modal_page()
        order_history.login_page_click_order_history()
        assert order_history.order_list_date_new_order().text

    def test_logout(self, driver, create_user):
        email = create_user.json()['user']['email']
        logout = LoginPage(driver)
        logout.main_page_click_to_login()
        logout.login_page_fill_email(email)
        logout.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        logout.login_page_log_in()
        logout.wait_close_modal_page()
        logout.main_page_click_to_login()
        logout.login_page_click_logout()
        logout.wait_close_modal_page()
        assert logout.login_page_title()
