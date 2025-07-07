# O! = 1
# n! = 1*2*3...n, n>0

# def fact(n):
#     factorial = 1
#     for i in range(2, n+1):
#         factorial *= i
#     return factorial

# print(fact(5))


# O! = 1
# n! = (1*2*3...(n-1)*n = (n-1)!*n

# def fact(n):
#     if n ==0:
#         return 1
#     return fact(n-1) * n

# print(fact(5))



# 1 1 2 3 5 8 13 21 34 - fib(9)
# fib(n) = fib(n-1) + fib(n-2), n - это индекс последовательности
# fib(9) = fib(8) + fib(7)

# from timeit import timeit

# def fib(n):
#     if n in (0, 1):
#         return 1
#     return fib(n-1) + fib(n-2)

# print(f'Среднее время вычисления: '
#       f'{round(timeit('fib(35)', number = 10, globals = globals())/10, 3)} сек.')

# timeit('fib(35)')
# print(fib(35))

from timeit import timeit

# def fib(n):
#     f_1, f = 1,1
#     for i in range(n-1):
#         f_1, f = f, f_1 +f
#     return f

# print(f'Среднее время вычисления: '
#       f'{round(timeit('fib(35)', number = 10, globals = globals())/10, 3)} сек.')

# def fib(n):
#     global count
#     count += 1
#     if n in (0, 1):
#         return 1
#     return fib(n-1) + fib(n-2)

# count = 0
# fib(35)
# print(count)

# from sys import setrecursionlimit
# setrecursionlimit(2000)
# def fib(n):
#     global count
#     count += 1
#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)
#     return cache[n]

# count = 0
# cache = {0:1, 1:1}

# # fib(35)
# # print(count)
# print(f'Среднее время вычисления: '
#       f'{round(timeit('fib(1000)', number = 10, globals = globals())/10, 3)} сек.')


# def countdown(n):
#     if n == 0:
#         print('Поехали')
#     else:
#         print(n)
#         countdown(n-1)
# print(countdown(10))


# factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1)
# 1

# 2 * 1 = 2
# 3 * 2 = 6
# 4 * 6 = 24
# factorial(4)
# factorial(3)


# def factorial(n, depth = 0):
#     print(" " * depth + f" factorial({n})")
#     if n == 1:
#         print(' ' * depth + f'  return 1')
#         return 1
#     else:
#         result = n * factorial(n-1, depth + 1)
#         print(" " * depth + f"  return {n} * factorial({n-1}) = {result}")
# factorial(4)


from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    if n in (0, 1):
        return 1
    return fib(n-1) + fib(n-2)

print(f'Среднее время вычисления: '
      f'{round(timeit('fib(35)', number = 10, globals = globals())/10, 3)} сек.')

