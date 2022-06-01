import pytest
from selenium import webdriver
from pages_Ampro.login_page import LoginPage
from base_Ampro.webdriverfactory import WebDriverFactory
import time

@pytest.fixture(scope="module")
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp=LoginPage(driver)
    # lp.login("pratishtha.bhadula@thesmartcube.com","Login#123") #test credentials
    lp.login("pratishtha.bhadula@thesmartcube.com","Aimforthemoon#22")
    time.sleep(2)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")
    
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")