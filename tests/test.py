import requests

url = "https://powerlessly-fragrant-scallop.cloudpub.ru/books"

# Данные, которые мы отправляем в запросе
data = {
    "title": "Новая книга",
    "author": "Мэттью"
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Проверяем успешность запроса
if response.status_code == 201:  # Обычно 201 Created означает успешное создание ресурса
    print("Книга успешно добавлена:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
