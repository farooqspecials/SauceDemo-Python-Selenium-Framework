from pages.login_page import LoginPage
from pages.menu_page import MenuPage


def test_logout(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    menu_page = MenuPage(driver)

    login_page.login("standard_user", "secret_sauce")

    menu_page.open_menu()

    menu_page.logout()

    #assert "saucedemo.com" in driver.current_url
    assert login_page.is_login_button_displayed()