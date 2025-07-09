# Напишите функцию update_config(config, **kwargs), которая принимает словарь config
#  и обновляет его значениями из kwargs. Функция должна возвращать обновленный словарь.
# Внимательно отнеситесь к копированию объекта.(подсказка)

# Пример использования:
# base_config = {"host": "localhost", "port": 8080, "debug": False}
# new_config = update_config(base_config, port=9000, debug=True, user="admin")
# print(f"Исходный конфиг: {base_config}")
# print(f"Обновленный конфиг: {new_config}")
# # Вывод:
# # Исходный конфиг: {'host': 'localhost', 'port': 8080, 'debug': False}
# # Обновленный конфиг: {'host': 'localhost', 'port': 9000, 'debug': True, 'user': 'admin'}

def update_config(config, **kwargs):
    new_config = config.copy()
    new_config.update(kwargs)
    return new_config

base_config = {"host": "localhost", "port": 8080, "debug": False}
new_config = update_config(base_config, port=9000, debug=True, user="admin")

print(f"Исходный конфиг: {base_config}")
print(f"Обновленный конфиг: {new_config}")