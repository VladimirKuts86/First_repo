# Напишите функцию average_numbers(*args), которая принимает любое количество аргументов
#  разных типов и вычисляет среднее арифметическое только для числовых аргументов
#  (int или float).


def average_numbers(*args):
    count = 0
    summa = 0
    for number in args:
        if isinstance(number, str):
            continue
        else:
            count += 1
            summa += number
    print(summa / count)
average_numbers(2, 5, "ABC", 7, 8.3, "gg")