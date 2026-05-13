from playwright.sync_api import Page


def test_google_title(page: Page):
    page.goto("https://www.google.com")

    title = page.title()

    print(f"Page title is: {title}")

    assert "google" in title