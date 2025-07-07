# На именованные аргументы
# Напишите функцию create_user_profile(name, city="Не указан"), 
# которая возвращает строку с профилем. Город является необязательным параметром.

def create_user_profile(name, city="Не указан"):
    print(f'Имя пользователя: {name}.\nГород пользователя: {city}')
create_user_profile(input())