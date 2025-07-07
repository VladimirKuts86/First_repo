# import itertools

# print(itertools.product("ABC", repeat=2))

# from itertools import product

# from itertools import count

# for value in count(0, 0.1):
#     if value <= 1:
#         print(round(value, 1))
#     else:
#         break

# from itertools import cycle

# max_len = 10
# s = ""
# for letter in cycle("ABC"):
#     if len(s) < max_len:
#         s += letter
#     else:
#         break
# print(s)

# from itertools import repeat

# result = list(repeat("ABC", 5))
# print(result)

# from itertools import accumulate

# for value in accumulate([1, 2, 3, 4, 5]):
#     print(value)

# from itertools import chain

# values = list(chain("АБВ", "ГДЕË", "ЖЗИЙК"))
# print(values)

# from itertools import chain

# values = list(chain.from_iterable(["АБВ", "ГДЕË", "ЖЗИЙК"]))
# print(values)

# from itertools import product

# values = list(product([1, 2, 3], "ABCD"))
# print(values)

# from itertools import product

# values = list(product([1, 2, 3], "ABCD", repeat=2))
# print(values)

# from itertools import permutations

# values = list(permutations("ABC", r = 2))
# print(values)

# from itertools import combinations

# values = list (combinations("ABC", r=3))
# print(values)

# from itertools import combinations_with_replacement

# values = list(combinations_with_replacement("ABC", r=2))
# print(values)

# for index, value in enumerate("ABC", 1):
#     print(index, value)

# print(list(zip("ABC", [1, 2, 3])))

# print(list(zip("ABCDE", [1, 2, 3])))

# print(list(zip("ABCDE", [1, 2, 3], strict=True)))

# from itertools import zip_longest

# print(list(zip_longest("ABCDE", [1, 2, 3], fillvalue="AAAA")))

