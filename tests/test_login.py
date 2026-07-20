from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.get_page_title() == "Products"