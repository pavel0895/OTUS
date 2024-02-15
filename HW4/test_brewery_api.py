import json
import pprint

import pytest
import requests

from HW4.conftest import brewery_url


def test_get_list_breweries(brewery_url):
    r = requests.get(f'{brewery_url}breweries')
    assert r.status_code == 200
    pprint.pprint(r.reason)


brewery_id = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
def test_post_brewery(brewery_url):
    data = {'country': 'Russia'}
    r = requests.post(f'{brewery_url}breweries/{brewery_id}', data=data)
    assert r.status_code == 404
    pprint.pprint(r.reason)

@pytest.mark.parametrize('by_type', ['nano', 'micro'])
def test_by_type(brewery_url, by_type):
    r = requests.get(f'{brewery_url}breweries?by_type=micro&per_page=3')
    assert r.status_code == 200
    pprint.pprint(r.reason)

@pytest.mark.parametrize('size', [5])
def test_by_type(brewery_url, size):
    r = requests.get(f'{brewery_url}breweries/random?size=5')
    assert 'application/json' in r.headers.get('content-type')
    pprint.pprint(r.json())
    pprint.pprint(r.reason)

def test_delete_meta(brewery_url):
    r = requests.delete(f'{brewery_url}meta?by_country = south_korea')
    assert r.status_code == 404
    pprint.pprint(r.status_code)
    pprint.pprint(r.reason)