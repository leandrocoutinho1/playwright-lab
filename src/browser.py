from playwright.sync_api import sync_playwright

def create_page(headless: bool = False):
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=headless,
        slow_mo=50
    )

    context = browser.new_context()
    page = context.new_page()

    return playwright, browser, context, page
