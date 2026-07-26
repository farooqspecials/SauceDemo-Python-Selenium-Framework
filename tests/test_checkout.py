from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_information(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    inventory_page.open_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_information(
        "Farooq",
        "Ahmed",
        "12345"
    )

    assert checkout_page.get_page_title() == "Checkout: Overview"