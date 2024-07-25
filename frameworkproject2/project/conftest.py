#cmmnd line for invoking various browsers at running time
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browsername = request.config.getoption("browser_name")
    if browsername == 'chrome':
        driver = webdriver.Chrome()
    elif browsername == 'firefox':
        print("firefox")
    elif browsername == 'IE':
        print("IE")
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
