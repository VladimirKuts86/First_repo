# numb = int(input())
# numb2 = int(input())
# print("Три числа {}, {}".format(numb, numb2))

# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:3])
# print(numbers[::-1])

# numbers[2 = 50]
# print(numbers)

# numbers.append(60)

# numbers = []
# for i in range(10):
#     numbers.append(int(input()))
# print(numbers)

# del numbers[-1]
# del numbers[::2]

# numbers = [10, 20, 30, 40, 50]
# numbers_2 = [11, 22]
# print(numbers + numbers_2)
# print(numbers * 2)
# print(len(numbers))

# a = [[1,2], [3, 4]]
# print(a[0[0]])

import copy

# a = [[1, 2], [3,4]]
# b = copy.deepcopy(a)
# b[0].append(999)
# print(a)
# print(b)

# numbers = (1, 2, 3, 4)
# numbers = (1, )
# numbers = 1, 2, 3, 4

a = 1
b = 2
a, b = b, a
print(f"a = {a}, b = {b}")
