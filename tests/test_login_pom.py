from playwright.sync_api import Page
from pages.login_page import LoginPage


def test_valid_login(page: Page):

    login = LoginPage(page)

    login.open_application()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    login.verify_login_success()