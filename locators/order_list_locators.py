from selenium.webdriver.common.by import By


class OrderListLocators:
    ORDER_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')
    FIRST_ORDER_FROM_LIST = (By.XPATH, '//ul/li[1][contains(@class, "OrderHistory") and contains(@class, "listItem")]')
    CONTAINS = (By.XPATH, '//p[text()="Cостав"]')
    READY_COUNT_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    READY_COUNT_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    DATE_ORDER = (By.XPATH, '//p[contains(text(),"Сегодня")]')



