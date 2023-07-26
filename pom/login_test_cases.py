import time


class Swag:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self):
        self.page.locator("[data-test=\"username\"]").click()
        self.page.locator("[data-test=\"username\"]").fill("standard_user")
        self.page.locator("[data-test=\"username\"]").press("Tab")
        self.page.locator("[data-test=\"password\"]").fill("secret_sauce")
        self.page.locator("[data-test=\"login-button\"]").click()
        time.sleep(3)

    def add_to_cart(self):
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        time.sleep(3)

    def remove_from_cart(self):
        self.page.locator("a").filter(has_text="1").click()
        self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
        time.sleep(3)

    def cont_shopping(self):
        self.page.locator("[data-test=\"continue-shopping\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        time.sleep(3)

    def checkout_cart(self):
        self.page.locator("a").filter(has_text="1").click()
        self.page.locator("[data-test=\"checkout\"]").click()
        time.sleep(3)

    def fill_form(self):
        self.page.locator("[data-test=\"firstName\"]").click()
        self.page.locator("[data-test=\"firstName\"]").fill("Abdul")
        self.page.locator("[data-test=\"firstName\"]").press("Tab")
        self.page.locator("[data-test=\"lastName\"]").fill("Ahad")
        self.page.locator("[data-test=\"postalCode\"]").click()
        self.page.locator("[data-test=\"postalCode\"]").fill("54000")
        self.page.locator("[data-test=\"continue\"]").click()
        self.page.locator("[data-test=\"finish\"]").click()
        self.page.locator("[data-test=\"back-to-products\"]").click()
        time.sleep(3)

    def log_out(self):
        self.page.get_by_role("button", name="Open Menu").click()
        self.page.get_by_role("link", name="Logout").click()
        time.sleep(3)
