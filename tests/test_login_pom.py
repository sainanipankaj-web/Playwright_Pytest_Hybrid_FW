from playwright.sync_api import Page
from pages.login_page import LoginPage

from config.settings import BASE_URL_SAUCEDEMO
from testdata.test_data import USERNAME,PASSWORD
import pytest


#@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.login
def test_valid_login_using_pom(login_page,screenshot_on_finish):

    # login = LoginPage(page)

    # login.open_application(BASE_URL_SAUCEDEMO)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    login_page.verify_login_success()

