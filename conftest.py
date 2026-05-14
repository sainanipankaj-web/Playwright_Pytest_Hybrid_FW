import pytest
from playwright.sync_api import Page
from config.settings import BASE_URL_SAUCEDEMO
import os


@pytest.fixture()
def login_page(page: Page):

    from pages.login_page import LoginPage

    login = LoginPage(page)

    login.open_application(BASE_URL_SAUCEDEMO)

    yield login

    print("\nTest completed")

@pytest.fixture()
def screenshot_on_finish( page, request):

    yield

    os.makedirs(
        "screenshots",
        exist_ok=True
    )

    test_name = request.node.name

    page.screenshot(
        path=
        f"screenshots/test_end_ss_{test_name}.png"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    
    outcome=yield

    report=outcome.get_result()


    if report.when=="call":

        if report.failed:

            page=item.funcargs.get(
                "page"
            )

            if page:

                os.makedirs(
                    "screenshots",
                    exist_ok=True
                )

                page.screenshot(
                    path=
                    f"screenshots/{item.name}.png"
                )