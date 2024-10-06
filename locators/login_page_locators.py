from selenium.webdriver.common.by import By


class LoginPageLocators:
    TITLE = (By.XPATH, '//h2[text() = "Вход"]')
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, '//a[text() = "Восстановить пароль"]')
    EMAIL_TEXT_FIELD = (By.XPATH, '//div/input[@name="name"]')
    PASSWORD_TEXT_FIELD = (By.XPATH, '//div/input[@name="Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    LOGIN_TEXT = (By.XPATH, '//div/label[text()="Логин"]/following-sibling::input')
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//button[text()="Выход"]')