class Data:
    valid_login = 'Izam123'
    valid_password = 'Qwerty123'
    valid_firstname = 'Izam'
    valid_courier_data = {'login': 'Izam123', 'password': 'Qwerty123', 'firstName': 'Izam'}
    courier_data_without_name = {'login': 'Izam12345', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Izam12345', 'password': '1234567'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Иван',
        'lastName': 'Петров',
        'address': 'Ленинградский проспект, 10',
        'metroStation': 5,
        'phone': '+79991234567',
        'rentTime': 2,
        'deliveryDate': '2025-02-15',
        'comment': 'Отличная погода сегодня!',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Анна',
        'lastName': 'Смирнова',
        'address': 'Москва, улица Лесная',
        'metroStation': 3,
        'phone': '+79161234567',
        'rentTime': 5,
        'deliveryDate': '2025-02-13',
        'comment': 'Тест.',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Мария',
        'lastName': 'Васильева',
        'address': 'Лаванда и Чабрец',
        'metroStation': 7,
        'phone': '+79990001122',
        'rentTime': 4,
        'deliveryDate': '2025-02-25',
        'comment': 'Тест',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Калантэ',
        'lastName': 'ArdRhena',
        'address': 'Пермякова',
        'metroStation': 20,
        'phone': '+77777777777',
        'rentTime': 2,
        'deliveryDate': '2024-06-27',
        'comment': 'Тест',
        'color': []
    }
