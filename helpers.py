from faker import Faker
import requests
import pytest
from urls import Urls

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def create_random_login():
    login = fake.text(max_nb_chars=7) + str(fake.random_int(0, 999))
    return login


def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_firstname():
    first_name = fakeRU.first_name()
    return first_name


@pytest.fixture
def create_courier():
    payload = {
        'login': create_random_login(),
        'password': create_random_password(),
        'firstName': create_random_firstname()
    }
    response = requests.post(Urls.URL_courier_create, data=payload)
    assert response.status_code == 201 and response.json() == {'ok': True}

    courier_id = requests.post(Urls.URL_courier_login, data={
        'login': payload['login'],
        'password': payload['password']
    }).json().get('id')

    yield payload, courier_id

    if courier_id:
        delete_response = requests.delete(f"{Urls.URL_courier_delete.replace(':id', str(courier_id))}")
        assert delete_response.status_code == 200 and response.json() == {'ok': True}