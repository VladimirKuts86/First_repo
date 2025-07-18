def my_sum(*numbers, start):
    summa = 0
    if start != None:
        summa += start
    for number in numbers:
        summa += number
    print(summa)

my_sum(*[42, -7, 3.14, 0, 1000, -256, 8.5, 17, -3, 99], start=4)

# my_sum(42, -7, 3.14, 0, 1000, -256, 8.5, 17, -3, 99)

def my_sum(numbers):
    summa = 0
    for item_1, item_2 in numbers:
    if start != None:
        summa += start
    for item_1 in numbers:
        number in item_1:
        summa += number
    print(summa)

my_sum([42, -7, 3.14, 0, 1000, -256, 8.5, 17, -3, 99], 4)