import pytest
import requests
import pprint

from HW4.conftest import json_url


def test_delete_users(json_url):
    response = requests.get(f'{json_url}users')
    assert response.status_code == 200
    pprint.pprint(response.reason)


def test_get_comments(json_url):
    response = requests.delete(f'{json_url}posts/1/comments?id=1')
    assert response.status_code == 404


def test_post_user(json_url):
    data = {'id': 'asd'}
    response = requests.post(f'{json_url}posts/1?id=1', data=data)
    assert response.status_code == 404


@pytest.mark.parametrize("id", [1, 2, 3])
def test_update_post(json_url, id):
    data = {
        "title": "Updated Title",
        "body": "This is the updated body."
    }
    response = requests.post(f'{json_url}posts', data=data)
    assert response.status_code == 201


@pytest.mark.parametrize("url", [("https://via.placeholder.com/600/92c952",
                                  "https://via.placeholder.com/600/771796"
                                  "https://via.placeholder.com/600/24f355")])
def test_photos_get(json_url, url):
    response = requests.get(f'{json_url}photos')
    assert response.status_code == 200
    pprint.pprint(response.reason)
