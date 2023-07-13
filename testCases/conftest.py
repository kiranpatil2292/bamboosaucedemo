import os
from datetime import datetime
import pytest

from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Kiran'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
