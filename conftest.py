import pytest
from selenium import webdriver

from data import StarBurgerData
from helper import Helper
from starburger_api import StarburgerApi


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.get(StarBurgerData.URL)
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.fixture()
def create_user():
    created_user = StarburgerApi.user_registration(Helper.create_random_registration_body())
    token = created_user.json()['accessToken']

    yield created_user

    StarburgerApi.delete_user(token)
