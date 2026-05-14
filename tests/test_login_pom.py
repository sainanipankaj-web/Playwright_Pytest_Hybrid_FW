from playwright.sync_api import Page
from pages.login_page import LoginPage

from config.settings import BASE_URL_SAUCEDEMO
from testdata.test_data import USERNAME,PASSWORD


def test_valid_login(page: Page):

    login = LoginPage(page)

    login.open_application(BASE_URL_SAUCEDEMO)

    login.login(
        USERNAME,
        PASSWORD
    )

    login.verify_login_success()