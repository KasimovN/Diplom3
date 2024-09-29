from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator_click):
        clicked_element = self.wait_and_find_element(locator_click)
        clicked_element.click()

    # @staticmethod
    # def scroll_page_to_footer(driver):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #
    # def click_cookie_button(self):
    #     cokkie_button = self.wait_and_find_element(MainPageLocators.COOKIE_BUTTON)
    #     cokkie_button.click()
