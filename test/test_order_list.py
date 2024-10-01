from selenium.webdriver import ActionChains

from api_data import ApiData
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_list_locators import OrderListLocators
from pages.main_page import MainPage


class TestOrderList:
    def test_full_order_information(self, driver):
        order_list = MainPage(driver)
        order_list.click_element(MainPageLocators.ORDER_LIST)
        order_list.click_element(OrderListLocators.FIRST_ORDER_FROM_LIST)
        assert order_list.wait_and_find_element(OrderListLocators.CONTAINS)

    def test_order_history_in_order_list(self, create_user, driver):
        email = create_user.json()['user']['email']
        create_order = MainPage(driver)
        actionchains = ActionChains(driver)
        create_order.click_element(MainPageLocators.ACCOUNT_BUTTON)
        create_order.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        create_order.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                        ApiData.BODY_USER_REGISTRATION['password'])
        create_order.click_element(LoginPageLocators.ENTER_BUTTON)
        element_from = create_order.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = create_order.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        actionchains.drag_and_drop(element_from, element_to).perform()
        create_order.click_element(MainPageLocators.ORDER)
        number = create_order.wait_and_find_element(MainPageLocators.ORDER_NUMBER).text
        create_order.click_element(MainPageLocators.ORDER_CLOSE_BUTTON)
        create_order.click_element(MainPageLocators.ORDER_LIST)
        assert create_order.wait_and_find_element(f'(By.XPATH, "//p[contains(text(),"{number}")]')

    def test_ready_counter_all_time(self, create_user, driver):
        email = create_user.json()['user']['email']
        actionchains = ActionChains(driver)
        ready_counter = MainPage(driver)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        ready_count = ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_ALL_TIME).text
        ready_counter.click_element(MainPageLocators.ACCOUNT_BUTTON)
        ready_counter.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        ready_counter.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                         ApiData.BODY_USER_REGISTRATION['password'])
        ready_counter.click_element(LoginPageLocators.ENTER_BUTTON)
        element_from = ready_counter.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = ready_counter.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        actionchains.drag_and_drop(element_from, element_to).perform()
        ready_counter.click_element(MainPageLocators.ORDER)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        assert int(ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_ALL_TIME).text) > int(ready_count)

    def test_ready_counter_today(self, create_user, driver):
        email = create_user.json()['user']['email']
        actionchains = ActionChains(driver)
        ready_counter = MainPage(driver)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        ready_count = ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_TODAY).text
        ready_counter.click_element(MainPageLocators.ACCOUNT_BUTTON)
        ready_counter.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        ready_counter.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                         ApiData.BODY_USER_REGISTRATION['password'])
        ready_counter.click_element(LoginPageLocators.ENTER_BUTTON)
        element_from = ready_counter.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = ready_counter.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        actionchains.drag_and_drop(element_from, element_to).perform()
        ready_counter.click_element(MainPageLocators.ORDER)
        ready_counter.click_element(MainPageLocators.ORDER_LIST)
        assert int(ready_counter.wait_and_find_element(OrderListLocators.READY_COUNT_TODAY).text) > int(ready_count)

    def test_current_order_in_work(self, create_user, driver):
        email = create_user.json()['user']['email']
        actionchains = ActionChains(driver)
        current_order = MainPage(driver)
        current_order.click_element(MainPageLocators.ACCOUNT_BUTTON)
        current_order.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        current_order.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                         ApiData.BODY_USER_REGISTRATION['password'])
        current_order.click_element(LoginPageLocators.ENTER_BUTTON)
        element_from = current_order.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = current_order.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        actionchains.drag_and_drop(element_from, element_to).perform()
        current_order.click_element(MainPageLocators.ORDER)
        number = current_order.wait_and_find_element(MainPageLocators.ORDER_NUMBER).text
        current_order.click_element(MainPageLocators.ORDER_CLOSE_BUTTON)
        current_order.click_element(MainPageLocators.ORDER_LIST)
        number_in_work = current_order.wait_and_find_element(f'(By.XPATH, "//ul[contains(@class, '
                                                             f'"orderListReady")]/li[text()="{number}"]').text
        assert number in number_in_work
