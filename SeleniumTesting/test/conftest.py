from selenium import webdriver
import pytest

# This allows you to call and create 
# py.test --browser_name chrome
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="firefix or chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption('browser_name')

    # Creating a driver browser
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path='..\\chromedriver.exe')
    elif browser_name == 'firefox':
        driver = webdriver.Chrome(executable_path='..\\geckodriver.exe')

    # Give driver an URL
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    # Maximize driver window
    driver.maximize_window()

    request.cls.driver = driver
    # Execute to close driver at the end of the proccess
    yield
    driver.close()
    