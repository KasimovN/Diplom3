import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from api_data import ApiData
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_list_locators import OrderListLocators
from pages.main_page import MainPage
from seletools.actions import drag_and_drop


class TestMainFeature:
    def test_constuctor_page(self, create_user, driver):
        email = create_user.json()['user']['email']
        constuctor_page = MainPage(driver)
        constuctor_page.click_element(MainPageLocators.ACCOUNT_BUTTON)
        constuctor_page.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        constuctor_page.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                           ApiData.BODY_USER_REGISTRATION['password'])
        constuctor_page.click_element(LoginPageLocators.ENTER_BUTTON)

        assert constuctor_page.wait_and_find_element(MainPageLocators.ORDER)

    def test_order_list(self, create_user, driver):
        email = create_user.json()['user']['email']
        order_list = MainPage(driver)
        order_list.click_element(MainPageLocators.ACCOUNT_BUTTON)
        order_list.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        order_list.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                      ApiData.BODY_USER_REGISTRATION['password'])
        order_list.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        order_list.click_element(MainPageLocators.ORDER_LIST)
        assert order_list.wait_and_find_element(OrderListLocators.ORDER_LIST)

    def test_ingredient_details(self, create_user, driver):
        email = create_user.json()['user']['email']
        ingredient_details = MainPage(driver)
        ingredient_details.click_element(MainPageLocators.ACCOUNT_BUTTON)
        ingredient_details.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        ingredient_details.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                              ApiData.BODY_USER_REGISTRATION['password'])
        ingredient_details.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        ingredient_details.click_element(MainPageLocators.KRATERNAY_BULKA)
        assert ingredient_details.wait_and_find_element(MainPageLocators.INGREDIEN_DETAILS)

    def test_ingredient_details_close_modal(self, create_user, driver):
        email = create_user.json()['user']['email']
        close_modal = MainPage(driver)
        close_modal.click_element(MainPageLocators.ACCOUNT_BUTTON)
        close_modal.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        close_modal.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                       ApiData.BODY_USER_REGISTRATION['password'])
        close_modal.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        close_modal.click_element(MainPageLocators.KRATERNAY_BULKA)
        close_modal.click_element(MainPageLocators.CLOSE_BUTTON_INGREDIENT_MODAL)
        assert close_modal.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)

    def test_drag_and_drop_ingredient(self, create_user, driver):
        email = create_user.json()['user']['email']
        close_modal = MainPage(driver)
        close_modal.click_element(MainPageLocators.ACCOUNT_BUTTON)
        close_modal.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        close_modal.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                       ApiData.BODY_USER_REGISTRATION['password'])
        close_modal.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        element_from = close_modal.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = close_modal.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        drag_and_drop(driver, element_from, element_to)
        close_modal.wait_and_find_element(MainPageLocators.INGREDIENT_COUNTER)
        assert close_modal.wait_and_find_element(MainPageLocators.INGREDIENT_COUNTER).text == '2'

    def test_create_order(self, create_user, driver):
        email = create_user.json()['user']['email']
        create_order = MainPage(driver)
        create_order.click_element(MainPageLocators.ACCOUNT_BUTTON)
        create_order.filling_text_field(LoginPageLocators.EMAIL_TEXT_FIELD, email)
        create_order.filling_text_field(LoginPageLocators.PASSWORD_TEXT_FIELD,
                                        ApiData.BODY_USER_REGISTRATION['password'])
        create_order.click_element(LoginPageLocators.ENTER_BUTTON)
        modal = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
        WebDriverWait(driver, 10).until_not(expected_conditions.visibility_of_element_located(modal))
        element_from = create_order.wait_and_find_element(MainPageLocators.KRATERNAY_BULKA)
        element_to = create_order.wait_and_find_element(MainPageLocators.TOP_BASKET_CONSTRUCTOR)
        drag_and_drop(driver, element_from, element_to)
        create_order.click_element(MainPageLocators.ORDER)
        assert create_order.wait_and_find_element(MainPageLocators.ORDER_IDENTIFICATION)
