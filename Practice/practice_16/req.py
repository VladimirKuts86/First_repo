# Get - получить данные
# POST - отправить данные
# PUT - полностью обновить ресурс
# DELETE -  удалить ресурс

import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response.json())

# url = 'https://jsonplaceholder.typicode.com/posts'
# data = {'title': 'foo', 'body': 'bar', 'userId': 1}

# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())

# params = {"userId":1}
# response = requests.get("https://jsonplaceholder.typicode.com/posts", params = params)
# print(response.url)
# print(response.json())

# headers = {'Autorization': 'Dearer YOR_TOKEN', 'User-Agent': 'my-app'}
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers=headers)
# print(response.json())

# session = requests.Session()
# session.headers.update({'Autorization': 'Dearer YOR_TOKEN'})

# response1 = session.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response1.json())

# response2 = session.get("https://jsonplaceholder.typicode.com/posts/2")
# print(response2.json())

# ConnectionError -  ошибка соединения
# Timeout -  превышено время ожидания ответа
# HTTPError - ошибка HTTP (404, 500)
# RequestsException - базовое исключение охватывающее все выше

# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
#     response.raise_for_status()
#     print(response.json())
# except requests.exceptions.HTTPError as http_er:
#     print(f'HTTP ошибка: {http_er}')
# except requests.exceptions.ConnectionError:
#     print('Ошибка соединения')
# except requests.exceptions.Timeout:
#     print('Превышено время ожидания')
# except requests.exceptions.RequestException as e:
#     print(f'Произошла ошибкаЖ {e}')

