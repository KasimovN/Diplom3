from locators.order_list_locators import OrderListLocators
from pages.login_page import LoginPage


class OrderListPage(LoginPage):
    def order_list_page_title(self):
        return self.wait_and_find_element(OrderListLocators.ORDER_LIST)

    def order_list_date_new_order(self):
        return self.wait_and_find_element(OrderListLocators.DATE_ORDER)

    def order_list_page_click_first_order(self):
        self.click_element(OrderListLocators.FIRST_ORDER_FROM_LIST)

    def order_list_page_order_contains(self):
        return self.wait_and_find_element(OrderListLocators.CONTAINS)

    def order_list_page_wait_and_find_counter_all_time(self):
        return self.wait_and_find_element(OrderListLocators.READY_COUNT_ALL_TIME)

    def order_list_page_wait_and_find_counter_today(self):
        return self.wait_and_find_element(OrderListLocators.READY_COUNT_TODAY)
