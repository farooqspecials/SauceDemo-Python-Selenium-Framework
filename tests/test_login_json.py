import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.json_reader import load_json

login_data = load_json("data/login_data.json")


@pytest.mark.parametrize("data", login_data)
def test_login(driver, data):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(
        data["username"],
        data["password"]
    )

    assert inventory_page.get_page_title() == "Products"