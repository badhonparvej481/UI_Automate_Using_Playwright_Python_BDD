from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@given("user is on OrangeHRM login page")
def step_open_login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open()


@when("user logs in with valid username and password")
def step_login(context):
    context.login_page.login("Admin", "admin123")


@then("user should see the dashboard page")
def step_verify_dashboard(context):
    context.login_page.verify_dashboard()
