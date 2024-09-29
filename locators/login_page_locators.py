from selenium.webdriver.common.by import By


class LoginPageLocators:
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[text() = "Восстановить пароль"]')