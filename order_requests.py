import requests
import configuration
import data

def create_order(body):
    """Создание нового заказа"""
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers_order)

def get_order_by_track(track_number):
    """Получение заказа по номеру трека"""
    params = {"track": track_number}
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
        params=params,
        headers=data.headers_order
    )