import requests
import allure
import pytest
import json
from data import OrderData
from urls import Urls


class TestOrderCreate:

    @allure.title('Cоздание заказа с разными параметрами цвета')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_grey_1,
        OrderData.order_data_black_2,
        OrderData.order_data_two_colors_3,
        OrderData.order_data_no_colors_4
    ])
    def test_create_order_with_different_color_options(self, order_data):
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.URL_orders_create, data=order_data, headers=headers, timeout=5)
        assert response.status_code == 201 and 'track' in response.text
