# Задание 1
# С использованием фреймворка pytest написать тест операции checkText
# SOAP API https://speller.yandex.net/services/spellservice?WSDL
# Тест должен использовать DDT и проверять наличие определенного
# верного слова в списке предложенных исправлений к определенному
# неверному слову.
# Слова должны быть заданы через фикстуры в testdata.py,
# адрес wsdl должен быть вынесен в testdata.yaml.
# Методы работы с SOAP должны быть вынесены в отдельную библиотеку.


from zeep import Client, Settings
import yaml

with open(r'C:\Users\Оля\PycharmProjects\pythonAPI2\Seminars\seminar1\config.yaml') as f:
    data = yaml.safe_load(f)

def check_word(word):
    url = data["url"]
    settings = Settings(strict=False)
    client = Client(wsdl=url, settings=settings)
    return client.service.checkText(word)[0]['s']

# Moto@mail.ru
# 14c1b84f87




