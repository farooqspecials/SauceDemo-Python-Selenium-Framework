from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)