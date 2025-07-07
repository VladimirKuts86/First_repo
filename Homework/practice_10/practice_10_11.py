# Напишите функцию sum_all(*numbers), которая принимает любое количество чисел и 
# возвращает их сумму.

from itertools import accumulate

def sum_all(*numbers):
    for summa in accumulate(numbers):
        print(summa)
sum_all(1, 2, 6, 89, 7)


def sum_all(*numbers):
    summa = 0
    for number in numbers:
        summa += number
    print(summa)
sum_all(1, 2, 6, 89, 7)