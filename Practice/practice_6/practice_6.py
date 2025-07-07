# numbers = [int(input()) for i in range(5)]
# avg = sum(numbers) // len(numbers)
# numbers = [element for element in numbers if element > avg]
# print(numbers)

# numbers = [int(input()) for i in range(5)]
# numbers = [element for element in numbers if element > sum(numbers) // len(numbers)]
# print(numbers)

# matrix = [[int(x) for x in input().split()] for i in range(5)]
# print(matrix)

matrix = []
for i in range(5):
    line = input()
    list_line = line.split()
    new_list = []
    for x in list_line:
        new_list.append(int(x))
    matrix.append(new_list)
print(matrix)

# zeros  = [[0] * 5 for i in range(5)]
# zeros[0][0] = 1
# print(zeros)

# text = 'Строка символов'
# codes = [ord(symbol) for symbol in text]
# print(codes)

# countries = {'Россия': ['русский'],
#              'Беларусь': ['белорусский', 'русский'],
#              'Бельгия': ['немецкий', 'французский', 'нидерландский'],
#              'Вьетнам': ['вьеинамский']}
# multiple_lang = [country for country, lang in countries.items() if len(lang) > 1]
# print(multiple_lang)

# countries = {country: capital for country, capital in 
#              [("Россия", "Москва"),
#               ("Беларусь", "Минск"),
#               ("Сербия", "Белград")]}
# print(countries)

# numbers = (int(input()) for i in range(5))
# print(numbers)

# from sys import getsizeof

# numbers_iter = (i for i in range(10**6))
# print(getsizeof(numbers_iter))

# numbers_list = list(range(10**6))
# print(getsizeof(numbers_list))

# from timeit import timeit

# print(round(timeit("s = '; '.join(str(x) for x in range(10**7))", number = 10), 3))
# print(round(timeit("s = '; '.join([str(x) for x in range(10**7)])", number = 10), 3))

