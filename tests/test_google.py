from playwright.sync_api import Page
import pytest

@pytest.mark.smoke
def test_google_title(page: Page, screenshot_on_finish):
    page.goto("https://www.google.com")

    title = page.title()

    print(f"Page title is: {title}")

    assert "google" in title.lower(), "Title does not contain 'google'"