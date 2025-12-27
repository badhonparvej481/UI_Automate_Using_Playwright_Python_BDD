# from playwright.sync_api import sync_playwright
# import time

# def before_all(context):
#     # Launch Playwright browser
#     context.playwright = sync_playwright().start()
#     context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
#     context.context = context.browser.new_context()
#     context.page = context.context.new_page()

# def after_all(context):
#     # Keep browser open for manual inspection
#     print("Test finished - browser will stay open for 10 minutes")
#     try:
#         time.sleep(600)  # wait 10 minutes
#     except KeyboardInterrupt:
#         print("Manual exit")
#     # Optional cleanup manually if needed:
#     # context.browser.close()
#     # context.playwright.stop()


from playwright.sync_api import sync_playwright
import time


def before_all(context):
    # Launch Playwright browser
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False, slow_mo=500)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()


def after_all(context):
    # Keep browser open for manual inspection
    print("Test finished - browser will stay open for 10 minutes")
    try:
        time.sleep(600)  # wait 10 minutes
    except KeyboardInterrupt:
        print("Manual exit")
    # Optional cleanup manually if needed:
    # context.browser.close()
    # context.playwright.stop()
