from playwright.sync_api import Playwright
from pom.login_test_cases import Swag


def test_swag_lab(page: Playwright):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # page = browser.new_page()
    sw = Swag(page)
    sw.navigate()
    sw.login()
    sw.add_to_cart()
    sw.remove_from_cart()
    sw.cont_shopping()
    sw.checkout_cart()
    sw.fill_form()
    sw.log_out()
    # page.screenshot(path="screenshot.png")
