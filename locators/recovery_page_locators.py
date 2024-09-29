
from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    EMAIL_TEXT_FIELD = (By.XPATH, '//input')
    RECOVERY_BUTTON = (By.XPATH, '//button[text() = "Восстановить"]')

    COD_FROM_MAIL = (By.XPATH, '//label[text() = "Введите код из письма"]/parent::div')
    VISIBLE_PASSWORD_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    PASSWORD_TEXT_FIELD = (By.XPATH, '//input[@name="Введите новый пароль"]')
