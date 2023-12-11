import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata["address"])


def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_lable = site.find_element("xpath", result_xpath)
    assert err_lable.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"

# test_step1()


# высота элемента
# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# # цвет элемента копируем по клику на код элемента копи икспас
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property("xpath", xpath, "color"))


# driver_path: chromedriver.exe в ямл если используем скаченный драйвер
