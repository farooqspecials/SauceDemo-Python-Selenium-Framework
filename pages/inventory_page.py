from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK)

    def get_cart_count(self):
        return self.get_text(self.CART_BADGE)

    def cart_badge_exists(self):
        try:
            self.driver.find_element(*self.CART_BADGE)
            return True
        except NoSuchElementException:
            return False

    def open_cart(self):
        self.click(self.CART_ICON)