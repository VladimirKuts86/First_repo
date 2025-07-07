# 12. Генератор чисел кратных 3 и 5
numbers = (x for x in range(1, 25) if x % 3 == 0 and x % 5 == 0)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break