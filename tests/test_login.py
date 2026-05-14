from playwright.sync_api import (Browser, Page,
expect)   



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
    expect(page.locator(".title")).to_have_text("Products")

     # save after login
    page.context.storage_state(
        path="login_state.json"
    )

    print("Session saved successfully")

    print("Login successful")


def test_login_with_session_info(browser: Browser):
    context = browser.new_context(storage_state="login_state.json")
    page = context.new_page()

    # Open application
    page.goto("https://www.saucedemo.com/inventory.html")

    # Assertion
    expect(page.locator(".title")).to_have_text("Products")

    context.close()
    print("Login successful")