# lst = [x**2 for x in range(11) if x% 2 == 0]
# print(lst)

# lst = ['even' if x % 2 == 0 else 'odd' for x in range(1, 11)]
# print(lst)

# lst = ['pass' if x >= 50 else 'fail' for x in [70, 40, 55, 50, 90, 100]]
# print(lst)

# lst = [x if x > 0 else 0 for x in [3, 5, 0, -10, -2, 34, 5, -11]]
# print(lst)

# scores = [70, 40, 55, 50, 90, 100]
# grades = [5 if x >= 90 else 4 if x >= 70 else 3 if x >= 55 else 2 for x in scores]
# print(grades)

# MEMORY

# x = [element ** 2 for element in range(5)]
# y = [element ** 2 for element in range(5)]
# print(x==y)
# print(x is y)

# numbers = [1, 2, 3]
# print(f"{numbers}, id = {id(numbers)}")
# numbers = numbers + [4]
# print(f"{numbers}, id = {id(numbers)}")

# x = [1, 2, 3]
# y = x
# print(x is y)
# x[0] = 0
# print(x)
# print(y)
# print(x is y)

# x = [1, 2, 3]
# y = x[:]
# print(x is y)
# x[0] = 0
# print(x)
# print(y)
# print(x is y)

# numbers = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]
# numbers_copy = numbers[:]
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

# numbers = [[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]
# numbers_copy = [elem[:] for elem in numbers]
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])
# print(numbers_copy)

# from copy import deepcopy

# numbers = [[1, 2, [0, 5, 55],
#            [4, 5, 6],
#            [7, 8, 9]]
# numbers_copy = deepcopy(numbers)
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

