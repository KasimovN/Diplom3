import time
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop

from api_data import ApiData
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_list_locators import OrderListLocators
from pages.main_page import MainPage


class TestOrderList:
    def test_full_order_information(self, driver):
        order_list = MainPage(driver)
        order_list.click_element(MainPageLocators.ORDER_LIST)  # Открываем "Лента заказов"
        order_list.click_element(OrderListLocators.FIRST_ORDER_FROM_LIST)
        assert order_list.wait_and_find_element(OrderListLocators.CONTAINS)

    def test_order_history_in_order_list(self, create_user, driver):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        create_order = MainPage(driver)
        create_order.click_element(MainPageLocators.ACCOUNT_BUTTON)
        create_order.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        create_order.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                        ApiData.BODY_USER_REGISTRATION['password'])
        create_order.click_element(LoginPageLocators.ENTER_BUTTON)  # Авторизовываемся
        create_order.wait_close_modal_page()
        element_from = create_order.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = create_order.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        drag_and_drop(driver, element_from, element_to)
        create_order.click_element(MainPageLocators.ORDER)  # Создаем заказ
        time.sleep(3)  # Костыль - для стальной отработки
        number = create_order.wait_and_find_element(MainPageLocators.ORDER_NUMBER).text  # Запоминаем номер заказа
        create_order.click_element(MainPageLocators.ORDER_CLOSE_BUTTON)
        create_order.click_element(MainPageLocators.ORDER_LIST)
        time.sleep(3)  # Костыль - для стальной отработки
        locator = f'//*[contains(text(),"{number}")]'
        assert create_order.wait_and_find_element((By.XPATH, locator))  # Проверяем, что новый заказ есть в ленте

    def test_ready_counter_all_time(self, create_user, driver):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        ready_counter = MainPage(driver)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        ready_count = ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_ALL_TIME).text
        ready_counter.click_element(MainPageLocators.ACCOUNT_BUTTON)
        ready_counter.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        ready_counter.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                         ApiData.BODY_USER_REGISTRATION['password'])
        ready_counter.click_element(LoginPageLocators.ENTER_BUTTON)  # Авторизовываемся
        ready_counter.wait_close_modal_page()
        element_from = ready_counter.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = ready_counter.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        drag_and_drop(driver, element_from, element_to)
        ready_counter.click_element(MainPageLocators.ORDER)  # Создаем заказ
        time.sleep(3)  # Костыль - для стальной отработки
        ready_counter.click_element(MainPageLocators.ORDER_CLOSE_BUTTON)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        # Проверка на увеличение счетчика заказов за все время при создании нового заказа
        assert int(ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_ALL_TIME).text) > int(ready_count)

    def test_ready_counter_today(self, create_user, driver):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        ready_counter = MainPage(driver)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        ready_count = ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_TODAY).text
        ready_counter.click_element(MainPageLocators.ACCOUNT_BUTTON)
        ready_counter.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        ready_counter.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                         ApiData.BODY_USER_REGISTRATION['password'])
        ready_counter.click_element(LoginPageLocators.ENTER_BUTTON)  # Авторизовываемся
        ready_counter.wait_close_modal_page()
        element_from = ready_counter.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = ready_counter.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        drag_and_drop(driver, element_from, element_to)
        ready_counter.click_element(MainPageLocators.ORDER)  # Создаем заказ
        time.sleep(3)  # Костыль - для стальной отработки
        ready_counter.click_element(MainPageLocators.ORDER_CLOSE_BUTTON)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        # Проверка на увеличение счетчика заказов за сегодня при создании нового заказа
        assert int(ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_TODAY).text) > int(ready_count)

    def test_current_order_in_work(self, create_user, driver):
        email = create_user.json()['user']['email']  # Создаем временного пользователя
        current_order = MainPage(driver)
        current_order.click_element(MainPageLocators.ACCOUNT_BUTTON)
        current_order.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        current_order.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                         ApiData.BODY_USER_REGISTRATION['password'])
        current_order.click_element(LoginPageLocators.ENTER_BUTTON)  # Авторизовываемся
        current_order.wait_close_modal_page()
        element_from = current_order.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = current_order.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        drag_and_drop(driver, element_from, element_to)  # Создаем заказ
        current_order.click_element(MainPageLocators.ORDER)
        time.sleep(3)  # Костыль - для стальной отработки
        number = current_order.wait_and_find_element(MainPageLocators.ORDER_NUMBER).text
        current_order.click_element(MainPageLocators.ORDER_CLOSE_BUTTON)
        current_order.click_element(MainPageLocators.ORDER_LIST)
        locator = (By.XPATH, f'//ul[contains(@class,"orderListReady")]/li[text()="{number}"]')
        number_in_work = current_order.wait_and_find_element(locator).text
        assert number in number_in_work  # Проверка, что созданный заказ в работе
