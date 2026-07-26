from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        return self.get_text(self.CART_ITEM)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)