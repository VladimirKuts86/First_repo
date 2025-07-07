# 14. Генератор координат сетки (x, y) 0–9 - (0, 0), (0, 1), ...,
numbers = ((i, j) for i in range(9) for j in range(9))
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

numbers = [(i, j) for i in range(9) for j in range(9)]
print(numbers)
