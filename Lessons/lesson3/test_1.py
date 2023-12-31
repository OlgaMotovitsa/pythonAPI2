from testpage import OperationsHelper
import logging
import yaml


with open(r"C:\Users\Оля\PycharmProjects\pythonAPI2\Seminars\seminar3\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"





