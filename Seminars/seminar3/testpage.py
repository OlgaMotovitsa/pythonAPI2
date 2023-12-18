from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


# класс поиска локаторов
class TestSearchLocators:
    #  — локатор поля ввода логина
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    # — локатор поля ввода пароля
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    # — локатор кнопки логина
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    # — локатор поля с ошибкой
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    #  локатор проверки что залогинились - проверка наличия слова BLOG на странице
    LOCATOR_RESULT_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    # локатор кнопки создания нового поста
    LOCATOR_CREATE_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
    # локатор поля - ввести название поста
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    # локатор поля - ввести содержание поста
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    # локатор кнопки создания/сохраниения поста
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    # локатор проверки создания нового поста - проверка на наличие слов - название поста
    LOCATOR_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")



# класс с методами (действиями с локаторами из файла test_1)

class OperationsHelper(BasePage):
    #  функция ввода логина
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    #  функция ввода пароля
    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    #  функция нажатия кнопки login
    def click_login_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    #  функция вывода текста (в нашем случае 401)
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    # функция поиска слова blog
    def get_text_blog(self):
        text_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=2)
        text = text_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_LOGIN[1]}")
        return text

    # функция нажатия на кнопку создания нового поста
    def click_nwe_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST).click()

    # функция ввода названия поста в поле
    def enter_title_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    # функция ввода содержимого поста в поле
    def enter_content_post(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    # функция нажатия кнопки создания/сохранения поста
    def click_create_nwe_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    # функция проверки наличия созданного поста- наличие названия поста
    def post(self):
        post_field = self.find_element(TestSearchLocators.LOCATOR_POST, time=2)
        text = post_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_POST[1]}")
        return text



