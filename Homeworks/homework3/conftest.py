import pytest
import yaml
# import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open(r"C:\Users\Оля\PycharmProjects\pythonAPI2\Seminars\seminar3\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="function")
def browser():
    if testdata['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif testdata['browser'] == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
