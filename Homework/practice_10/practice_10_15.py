# Напишите функцию print_attributes(**kwargs), которая принимает любые именованные
#  аргументы и выводит их в формате "ключ: значение".

def print_attributes(**kwargs):
    [print(f'{key} : {value}') for key, value in kwargs.items()]
print_attributes(fruit="orange", vegetables="cucumber", berry="roseberry")

