from playwright.sync_api import Page, expect

from utils.logger import get_logger

logger=get_logger()


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")
        self.products_title = page.get_by_text("Productsss")

    def open_application(self, url):
        logger.info(
        "Opening application"
        )   
        self.page.goto(url)

    def login(self, username, password):
        logger.info("Filling login credentials")
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def verify_login_success(self):
        logger.info("Verifying login success")
        expect(self.products_title).to_be_visible()