from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger()


def test_successful_login(driver):

    logger.info("===== Starting Login Test =====")

    driver.get("https://www.saucedemo.com/")
    logger.info("Opened SauceDemo website")

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    logger.info("Logging in with standard_user")
    login_page.login("standard_user", "secret_sauce")

    logger.info("Verifying Inventory page")
    assert inventory_page.get_page_title() == "Products"

    logger.info("Login Test Passed")