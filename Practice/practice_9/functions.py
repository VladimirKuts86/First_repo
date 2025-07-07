# def only_even(numbers):
#     result = True
#     for x in numbers:
#         if x % 2 != 0:
#             result = False
#             break
#     return result
# print(only_even([2, 4, 6]))
# print(only_even([2, 4, 5]))

# def only_even(numbers):
#     for x in numbers:
#         if x % 2 != 0:
#             return False
#     return True
# print(only_even([2, 4, 6]))
# print(only_even([2, 4, 5]))

# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True
# print(only_even([2, 4, 6]))
# print(only_even([2, 4, 5]))

# a, b = only_even([2, 4, 5])
# print(a)
# print(b)

# def check_password(pwd):
#     return pwd == password

# password = "Python"
# print(check_password('1, 2, 3'))

# def list_modify():
#     del sample[-1]

# sample = [1, 2, 3]
# list_modify()
# print(sample)

# def list_modify():
#     sample = [4, 5, 6]

# sample = [1,2,3]
# list_modify()
# print(sample)

# def list_modify_1(list_arg):
#     #создаем новый локальный список не имеющий связи с внешним
#     list_arg = [1, 2, 3, 4]

# def list_modify_2(list_arg):
#     #меняем исходный внешний список, переданный как аргумент
#     list_arg += [4]

# sample_1 = [1, 2, 3]
# sample_2 = [1, 2, 3]

# list_modify_1(sample_1)
# list_modify_2(sample_2)
# print(sample_1)
# print(sample_2) 


# def inc():
#     global x
#     x += 1
#     print(f'Количество выводов функции равно {x}.')
# x = 0
# inc()
# inc()
# inc()


# def f(count):
#     count += 1
#     print(f'Количество выводов функции равно {count}.')
#     return count
# count_f = 0
# count_f = f(count_f)
# count_f = f(count_f)
# count_f = f(count_f)








# def only_pos(x):
#     return x >0

# result = filter(only_pos, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))


# result = filter(str.isalpha, '12345ABCDefgh$()@@')
# print("".join(result))


# def square(x):
#     return x ** 2
# result = map(square, range(5))
# print(", ".join(str(x) for x in result))


# result = map(str.lower, ["abCDF", "EFGh", "IJkl"])
# print('\n'.join(result))


# numbers = list(map(int, input().split()))
# print(numbers)


# result = filter(lambda x: x > 0, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))


# result = map(lambda x: x ** 2, range(5))
# print(", ".join(str(x) for x in result))


# lines = ['abcd', 'ab', 'abc', 'abcdef']
# print(sorted(lines, key = lambda line: len(line)))


# lines = ['abcd', 'ab', 'abc', 'abcdef', 'ba']
# print(sorted(lines, key = lambda line: (-len(line), line)))


# lines = ['abcd', 'abc', 'ba', 'ab', 'acde']
# print(min(lines, key = lambda line:  (-len(line), line)))


# result = (x for x in [-1, 5, 6, -10, 0] if x > 0)
# print(", ".join(str(x) for x in result))


# from functools import reduce

# numbers = range(1, 6)
# print(reduce(lambda x, y: x + y, numbers))