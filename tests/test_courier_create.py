import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname, create_courier

class TestCourierCreate:

    @allure.title('Создание аккаунта с валидными данными')
    def test_create_courier_success_valid_data(self, create_courier):
        payload, _ = create_courier
        assert payload is not None

    @allure.title('Повторное использование логина для создания курьера')
    def test_create_courier_duplicate_login_error(self, create_courier):
        payload, _ = create_courier
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 409
        assert response.json()['message'] == Data.error_messages['duplicate_login']

    @allure.title('Незаполненные обязательные поля')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_missing_required_fields_error(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, data=empty_credentials)
        assert response.status_code == 400
        assert response.json()['message'] == Data.error_messages['empty_input_create']
