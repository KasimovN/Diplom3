class TestOrderList:
    def test_full_order_information(self, driver):
        order_list = RecoveryPage(driver)
        order_list.click_element(MainPageLocators.ACCOUNT_BUTTON)
