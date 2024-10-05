import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator_click):
        clicked_element = self.wait_and_find_element(locator_click)
        clicked_element.click()

    def filling_text_field(self, filling_locator, filling_text):
        filled_element = self.wait_and_find_element(filling_locator)
        filled_element.send_keys(filling_text)

    def wait_close_modal_page(self):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.
                                                 visibility_of_element_located(MainPageLocators.MODAL))
