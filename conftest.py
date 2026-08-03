import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, edge or firefox"
    )


@pytest.fixture()
def driver(request):

    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = Options()
        options.add_argument("--incognito")
        
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()
            ),
             options=options
        )

    elif browser == "edge":

        driver = webdriver.Edge(
            service=EdgeService(
                EdgeChromiumDriverManager().install()
            )
        )

    elif browser == "firefox":

    
        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install()
            ),
            options=options
        )

    else:
        raise ValueError(
            f"Unsupported browser: {browser}"
        )

    driver.maximize_window()

    yield driver

    driver.quit()