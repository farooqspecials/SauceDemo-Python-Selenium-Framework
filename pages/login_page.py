from selenium.webdriver.common.by import By


class LoginPage:

    # ==========================
    # Locators
    # ==========================
    USERNAME_TEXTBOX = (By.ID, "user-name")
    PASSWORD_TEXTBOX = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """
        Constructor receives the WebDriver instance
        from the test.
        """
        self.driver = driver

    # ==========================
    # Action Methods
    # ==========================

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_TEXTBOX).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_TEXTBOX).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # ==========================
    # Business Method
    # ==========================

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()