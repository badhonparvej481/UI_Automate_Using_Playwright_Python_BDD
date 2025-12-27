from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"

    def open(self):
        self.page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        self.page.wait_for_selector(self.username_input)
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        # wait for dashboard URL
        self.page.wait_for_url("**/dashboard**")

    def verify_dashboard(self):
        assert "/dashboard" in self.page.url, f"Expected '/dashboard' in URL but got {self.page.url}"
