# Генератор квадратов числе до миллиона
square_of_number = (number**2 for number in range(1, 10**6))
while True:
    try:
        print(next(square_of_number))
    except StopIteration:
        break