from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_product_visible_in_cart(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    inventory_page.open_cart()

    assert cart_page.get_product_name() == "Sauce Labs Backpack"