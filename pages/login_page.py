from pages.base_page import BasePage


class LoginPage(BasePage):
    def filling_text_field(self, filling_locator, filling_text):
        filled_element = self.wait_and_find_element(filling_locator)
        filled_element.send_keys(filling_text)
