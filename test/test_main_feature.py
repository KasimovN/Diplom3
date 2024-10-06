from api_data import ApiData
from pages.login_page import LoginPage
from seletools.actions import drag_and_drop
from pages.order_list import OrderListPage


class TestMainFeature:
    def test_constuctor_page(self, create_user, driver):
        email = create_user.json()['user']['email']
        constuctor_page = LoginPage(driver)
        constuctor_page.main_page_click_to_login()
        constuctor_page.login_page_fill_email(email)
        constuctor_page.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        constuctor_page.login_page_log_in()
        constuctor_page.wait_close_modal_page()
        assert constuctor_page.main_page_wait_and_find_order_button()

    def test_order_list(self, create_user, driver):
        email = create_user.json()['user']['email']
        order_list = OrderListPage(driver)
        order_list.main_page_click_to_login()
        order_list.login_page_fill_email(email)
        order_list.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        order_list.login_page_log_in()
        order_list.wait_close_modal_page()
        order_list.main_page_click_order_list()
        assert order_list.order_list_page_title()

    def test_ingredient_details(self, create_user, driver):
        email = create_user.json()['user']['email']
        ingredient_details = LoginPage(driver)
        ingredient_details.main_page_click_to_login()
        ingredient_details.login_page_fill_email(email)
        ingredient_details.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        ingredient_details.login_page_log_in()
        ingredient_details.wait_close_modal_page()
        ingredient_details.main_page_click_kraternaya_bulka()
        assert ingredient_details.main_page_wait_and_find_detail_ingredient_info()

    def test_ingredient_details_close_modal(self, create_user, driver):
        email = create_user.json()['user']['email']
        close_modal = LoginPage(driver)
        close_modal.main_page_click_to_login()
        close_modal.login_page_fill_email(email)
        close_modal.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        close_modal.login_page_log_in()
        close_modal.wait_close_modal_page()
        close_modal.main_page_click_kraternaya_bulka()
        close_modal.main_page_click_close_button_detail_ingredient()
        assert close_modal.main_page_wait_and_find_kraternaya_bulka()

    def test_drag_and_drop_ingredient(self, create_user, driver):
        email = create_user.json()['user']['email']
        add_ingredient = LoginPage(driver)
        add_ingredient.main_page_click_to_login()
        add_ingredient.login_page_fill_email(email)
        add_ingredient.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        add_ingredient.login_page_log_in()
        add_ingredient.wait_close_modal_page()
        element_from = add_ingredient.main_page_wait_and_find_kraternaya_bulka()
        element_to = add_ingredient.main_page_wait_and_find_basket()
        drag_and_drop(driver, element_from, element_to)
        add_ingredient.main_page_wait_and_find_ingredient_counter()
        assert add_ingredient.main_page_wait_and_find_ingredient_counter().text == '2'

    def test_create_order(self, create_user, driver):
        email = create_user.json()['user']['email']
        create_order = LoginPage(driver)
        create_order.main_page_click_to_login()
        create_order.login_page_fill_email(email)
        create_order.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        create_order.login_page_log_in()
        create_order.wait_close_modal_page()
        element_from = create_order.main_page_wait_and_find_kraternaya_bulka()
        element_to = create_order.main_page_wait_and_find_basket()
        drag_and_drop(driver, element_from, element_to)
        create_order.main_page_click_order_button()
        assert create_order.main_page_wait_and_find_order_identification
