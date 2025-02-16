import pytest
import requests
from helpers import create_random_login, create_random_password, create_random_firstname
from urls import Urls


@pytest.fixture
def create_and_delete_courier():
    payload = {
        'login': create_random_login(),
        'password': create_random_password(),
        'firstName': create_random_firstname()
    }

    response = requests.post(Urls.URL_courier_create, data=payload)
    courier_id = requests.post(Urls.URL_courier_login, data={
        'login': payload['login'],
        'password': payload['password']
    }).json().get('id')

    yield payload, response

    if courier_id:
        requests.delete(f"{Urls.URL_courier_delete.replace(':id', str(courier_id))}")
