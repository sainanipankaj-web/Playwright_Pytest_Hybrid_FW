import pytest
from playwright.sync_api import Page
from config.settings import BASE_URL_SAUCEDEMO


@pytest.fixture()
def login_page(page: Page):

    from pages.login_page import LoginPage

    login = LoginPage(page)

    login.open_application(BASE_URL_SAUCEDEMO)

    yield login

    print("\nTest completed")

@pytest.fixture()
def screenshot_on_finish(page):

    yield

    page.screenshot(
        path="screenshots/end.png"
    )