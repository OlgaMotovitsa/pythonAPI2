import pytest
import yaml
import requests

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address_1"], data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]

@pytest.fixture()
def find_id():
    return 90547

@pytest.fixture()
def title():
    return "Homework1"

@pytest.fixture()
def description():
    return "The best homework"

@pytest.fixture()
def content():
    return "it`s just a begining!"

@pytest.fixture()
def find_description():
    return "The best homework"

