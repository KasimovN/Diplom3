from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def main_page_click_to_login(self):
        self.click_element(MainPageLocators.ACCOUNT_BUTTON)

    def main_page_wait_and_find_kraternaya_bulka(self):
        return self.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)

    def main_page_click_kraternaya_bulka(self):
        self.click_element(MainPageLocators.KRATERNAY_BULKA)

    def main_page_wait_and_find_basket(self):
        return self.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)

    def main_page_wait_and_find_ingredient_counter(self):
        return self.wait_and_find_element(MainPageLocators.INGREDIENT_COUNTER)

    def main_page_wait_and_find_detail_ingredient_info(self):
        return self.wait_and_find_element(MainPageLocators.INGREDIEN_DETAILS)

    def main_page_click_close_button_detail_ingredient(self):
        self.click_element(MainPageLocators.CLOSE_BUTTON_INGREDIENT_MODAL)

    def main_page_wait_and_find_order_button(self):
        return self.wait_and_find_element(MainPageLocators.ORDER)

    def main_page_click_order_button(self):
        self.click_element(MainPageLocators.ORDER)

    def main_page_wait_and_find_order_identification(self):
        return self.wait_and_find_element(MainPageLocators.ORDER_IDENTIFICATION)

    def main_page_wait_and_find_order_number(self):
        return self.wait_and_find_element(MainPageLocators.ORDER_NUMBER)

    def main_page_click_order_list(self):
        self.click_element(MainPageLocators.ORDER_LIST)

    def main_page_click_close_order_modal(self):
        self.click_element(MainPageLocators.ORDER_CLOSE_BUTTON)
