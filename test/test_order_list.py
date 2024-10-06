import time
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop
from api_data import ApiData
from locators.main_page_locators import MainPageLocators
from pages.order_list import OrderListPage


class TestOrderList:
    def test_full_order_information(self, driver):
        order_list = OrderListPage(driver)
        order_list.main_page_click_order_list()
        order_list.order_list_page_click_first_order()
        assert order_list.order_list_page_order_contains()

    def test_order_history_in_order_list(self, create_user, driver):
        email = create_user.json()['user']['email']
        create_order = OrderListPage(driver)
        create_order.main_page_click_to_login()
        create_order.login_page_fill_email(email)
        create_order.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        create_order.login_page_log_in()
        create_order.wait_close_modal_page()
        element_from = create_order.main_page_wait_and_find_kraternaya_bulka()
        element_to = create_order.main_page_wait_and_find_basket()
        drag_and_drop(driver, element_from, element_to)
        create_order.main_page_click_order_button()
        time.sleep(3)  # Костыль - для стальной отработки
        number = create_order.main_page_wait_and_find_order_number().text
        create_order.main_page_click_close_order_modal()
        create_order.main_page_click_order_list()
        time.sleep(3)  # Костыль - для стальной отработки
        locator = f'//*[contains(text(),"{number}")]'
        assert create_order.wait_and_find_element((By.XPATH, locator))

    def test_ready_counter_all_time(self, create_user, driver):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        ready_counter = OrderListPage(driver)
        ready_counter.main_page_click_order_list()
        ready_count = ready_counter.order_list_page_wait_and_find_counter_all_time().text
        ready_counter.main_page_click_to_login()
        ready_counter.login_page_fill_email(email)
        ready_counter.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        ready_counter.login_page_log_in()
        ready_counter.wait_close_modal_page()
        element_from = ready_counter.main_page_wait_and_find_kraternaya_bulka()
        element_to = ready_counter.main_page_wait_and_find_basket()
        drag_and_drop(driver, element_from, element_to)
        ready_counter.main_page_click_order_button()
        time.sleep(3)  # Костыль - для стальной отработки
        ready_counter.main_page_click_close_order_modal()
        ready_counter.main_page_click_order_list()
        assert int(ready_counter.order_list_page_wait_and_find_counter_all_time().text) > int(ready_count)

    def test_ready_counter_today(self, create_user, driver):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        ready_counter = OrderListPage(driver)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        ready_count = ready_counter.order_list_page_wait_and_find_counter_today().text
        ready_counter.main_page_click_to_login()
        ready_counter.login_page_fill_email(email)
        ready_counter.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        ready_counter.login_page_log_in()
        ready_counter.wait_close_modal_page()
        element_from = ready_counter.main_page_wait_and_find_kraternaya_bulka()
        element_to = ready_counter.main_page_wait_and_find_basket()
        drag_and_drop(driver, element_from, element_to)
        ready_counter.main_page_click_order_button()
        time.sleep(3)  # Костыль - для стальной отработки
        ready_counter.main_page_click_close_order_modal()
        ready_counter.main_page_click_order_list()
        # Проверка на увеличение счетчика заказов за сегодня при создании нового заказа
        assert int(ready_counter.order_list_page_wait_and_find_counter_today().text) > int(ready_count)

    def test_current_order_in_work(self, create_user, driver):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        current_order = OrderListPage(driver)
        current_order.main_page_click_to_login()
        current_order.login_page_fill_email(email)
        current_order.login_page_fill_password(ApiData.BODY_USER_REGISTRATION['password'])
        current_order.login_page_log_in()
        current_order.wait_close_modal_page()
        element_from = current_order.main_page_wait_and_find_kraternaya_bulka()
        element_to = current_order.main_page_wait_and_find_basket()
        drag_and_drop(driver, element_from, element_to)  # Создаем заказ
        current_order.main_page_click_order_button()
        time.sleep(3)  # Костыль - для стальной отработки
        number = current_order.main_page_wait_and_find_order_number().text
        current_order.main_page_click_close_order_modal()
        current_order.main_page_click_order_list()
        locator = (By.XPATH, f'//ul[contains(@class,"orderListReady")]/li[text()="{number}"]')
        number_in_work = current_order.wait_and_find_element(locator).text
        assert number in number_in_work  #
