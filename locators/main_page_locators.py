from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]')
    LOGO_BUTTON = (By.XPATH, '//a[@class="active"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    CONSTRUCT_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')
    ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_LIST = (By.XPATH, '//a[@href="/feed"]')
    KRATERNAY_BULKA = (By.XPATH, '//p[contains(text(),"Краторная булка")]')
    INGREDIEN_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CLOSE_BUTTON_INGREDIENT_MODAL = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    TOP_BASKET_CONSTRUCTOR = (By.XPATH, '//div[contains(@class, "constructor-element") and contains(@class, "top")]')
    INGREDIENT_COUNTER = (By.XPATH, '//p[text()="Краторная булка N-200i"]/parent::a/div[contains(@class, "counter")]/p')
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal") and contains(@class, "digits-large")]')
    ORDER_IDENTIFICATION = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_CLOSE_BUTTON = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    TIK_ANIMATION = (By.XPATH, '//img[@alt="tick animation"]')
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
