# Серёгина Анастасия, 43 когорта — Финальный проект. Инженер по тестированию плюс
import data
import order_requests


def test_create_and_get_order():
    """Создание заказа и получение его по треку"""

    # Создаём заказ
    create_response = order_requests.create_order(data.order_data)
    assert create_response.status_code == 201, f"Ожидался код 201, получен {create_response.status_code}"

    # Сохраняем трек заказа
    track_number = create_response.json().get("track")
    assert track_number is not None, "Трек не был получен при создании заказа"
    print(f"Номер трека: {track_number}")

    # Запрашиваем заказ по треку
    get_response = order_requests.get_order_by_track(track_number)

    # Проверяем, что код ответа равен 200
    assert get_response.status_code == 200, f"Ожидался код 200, получен {get_response.status_code}"

    print("Успех!")