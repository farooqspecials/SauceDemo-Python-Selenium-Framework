from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_finish_order(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = CheckoutOverviewPage(driver)

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    inventory_page.open_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_information(
        "Farooq",
        "Ahmed",
        "12345"
    )

    overview_page.click_finish()

    assert overview_page.get_complete_message() == "Thank you for your order!"