# Генерация пар i,j где i!=j
numbers = [(i, j) for i in range(3) for j in range(3) if i !=j]
print(numbers)

numbers = ((i, j) for i in range(3) for j in range(3) if i !=j)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break