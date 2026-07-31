import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ]
)
def test_login(driver, username, password):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(username, password)

    assert inventory_page.get_page_title() == "Products"