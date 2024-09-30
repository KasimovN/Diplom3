from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    LOGO_BUTTON = (By.XPATH, '//a[@class="active"]')
