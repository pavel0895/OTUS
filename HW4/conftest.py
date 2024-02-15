import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="Base URL for the test")
    parser.addoption("--status_code", action="store", default=200, type=int, help="Expected status code for the test")


@pytest.fixture
def dog_url():
    return 'https://dog.ceo/api/'

@pytest.fixture
def brewery_url():
    return 'https://api.openbrewerydb.org/v1/'

@pytest.fixture
def json_url():
    return 'https://jsonplaceholder.typicode.com/'