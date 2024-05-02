# Боев Виталий, 15-я когорта — Дипломный проект

import configuration
import requests

# Создание заказа
def create_order_request(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


# Получение заказа по номеру трекера
def get_order_request(track_number):
    get_order_url = f"{configuration.URL_SERVICE}{configuration.TRACK_ORDERS}?t={track_number}"
    response = requests.get(get_order_url)
    return response
