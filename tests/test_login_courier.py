import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierLogin:

    @allure.title('Упешная авторизация курьера при вводе валидных данных')
    def test_courier_successful_login_valid_data(self):
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Ошибка авторизации при вводе невалидных данных')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_invalid_data_error(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        assert response.status_code == 404
        response.json() ['message'] == 'Учетная запись не найдена'

    @allure.title('Авторизация с пустым полем логина или пароля')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_missing_credentials_error(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        assert response.status_code == 400
        response.json() ['message'] == 'Недостаточно данных для входа'
