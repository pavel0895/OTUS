import pytest
import requests
import pprint

from HW4.conftest import dog_url


def test_successful_response(dog_url):
    response = requests.get(f'{dog_url}breeds/list/all')
    assert response.status_code == 200
    pprint.pprint(response.reason)


def test_all_breeds_present(dog_url):
    response = requests.get(f'{dog_url}breeds/list/all')
    data = response.json()
    assert 'message' in data
    pprint.pprint(response.reason)


def test_random_image_response(dog_url):
    response = requests.get(f'{dog_url}breeds/image/random')
    assert response.status_code == 200
    pprint.pprint(response.reason)


@pytest.mark.parametrize("breed", ["bulldog", "poodle", "hound"])
def test_sub_breeds(dog_url, breed):
    link = f'{dog_url}breeds/list'
    response = requests.get(link)
    assert response.status_code == 200
    pprint.pprint(response.reason)

@pytest.mark.parametrize("afghan", [("https://images.dog.ceo/breeds/hound-afghan/n02088094_11432.jpg",
                                     "https://images.dog.ceo/breeds/hound-afghan/n02088094_482.jpg",
                                     "https://images.dog.ceo/breeds/hound-afghan/n02088094_8682.jpg")])
def test_sub_breed_images_response(dog_url, afghan):
    response = requests.get(f'{dog_url}breed/hound/afghan/images/random/3')
    data = response.json()
    assert data['status'] == 'success'
    pprint.pprint(response.reason)
