from playwright.sync_api import Page


def test_valid_login(page: Page):

    # Open application
    page.goto("https://www.saucedemo.com")

    # Enter username
    page.locator("#user-name").fill("standard_user")

    # Enter password
    page.locator("#password").fill("secret_sauce")

    # Click login button
    page.locator("#login-button").click()

    # Assertion
    assert page.locator(".title").text_content() == "Products"

    print("Login successful")