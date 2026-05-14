from datetime import datetime
from xmlrpc import client

import pytest
from playwright.sync_api import Page
from config.settings import BASE_URL_SAUCEDEMO
import os
import allure
from api.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():

    client = APIClient()

    yield client

    client.session.close()


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
def pytest_runtest_makereport(
        item,
        call
):

    outcome = yield

    report = outcome.get_result()


    if report.when == "call":

        if report.failed:

            page = item.funcargs.get(
                "page"
            )

            if page:

                os.makedirs(
                    "screenshots",
                    exist_ok=True
                )

                timestamp = datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                )

                file_name = (
                    f"{item.name}_{timestamp}.png"
                )

                screenshot_path = (
                    f"screenshots/{file_name}"
                )

                # Save in folder
                page.screenshot(
                    path=screenshot_path
                )

                # Attach same file to Allure
                allure.attach.file(
                    screenshot_path,

                    name=f"{item.name}_failure",

                    attachment_type=
                    allure.attachment_type.PNG
                )

@pytest.fixture(scope="session")
def api_client():

    client = APIClient()

    yield client

    client.session.close()