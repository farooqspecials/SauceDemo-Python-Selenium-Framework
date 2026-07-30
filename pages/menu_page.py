import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuPage(BasePage):

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu(self):
        self.click(self.MENU_BUTTON)
        time.sleep(1)


    def logout(self):
        self.click(self.LOGOUT_BUTTON)