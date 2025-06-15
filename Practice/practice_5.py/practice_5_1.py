# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# print(vowels)
# print(type(vowels))

# empty_set = set()
# print(len(empty_set))

# word = "коллекция"
# letters = set(word)
# print(letters)

# Объединение множеств
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_union = s_1.union(s_2) # s_1 | s_2
# print(s_union)

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_intersection = s_1.intersection(s_2) # s_1 & s_2
# print(s_untersection)

# Разность множеств
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_dif = s_1.difference(s_2) #  s_1 - s_2
# print(s_dif)

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_sym_dif = s_1.symmetric_difference(s_2) # s_1 ^ s_2
# print(s_sym_dif)

# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# letters = set("коллекция")
# print(", ".joim(letters & vowels))

# s_1 = {1, 2, 3}
# s_2 = {3, 1, 2}
# print(s_1 == s_2)

# s_1 = {1, 2, 3}
# s_2 = {1, 2, 3, 4}
# print(s_1 <= s_2)

# s_1 = {1, 2, 3, 4}
# s_2 = {1, 2, 3}
# print(s_1 >= s_2)

# countries_and_capitals = [("Россия", "Москва"), ("США", "Вашингтон"), ("Франция", "Париж")]
# for country in countries_and_capitals:
#     if country[0] == "Франция":
#         print(country[1])
#         break

# countries_and_capitals = {"Россия" : "Москва", 
#                           "США" : "Вашингтон",
#                           "Франция" : "Париж"}
# print(countries_and_capitals["Франция"])
# countries_and_capitals["Сербия"] = "Белград"
# print(countries_and_capitals)

# d = {"key" : "old_value"}
# d["key"] = "new_value"
# print(d['key'])

# countries_and_capitals = {"Россия" : "Москва", 
#                            "США" : "Вашингтон",
#                            "Франция" : "Париж"}
# if "Сербия" in countries_and_capitals:
#     print(countries_and_capitals['Сербия'])
# else:
#     print("Страна пока не добавлена в словарь")

# countries_and_capitals = {"Россия" : "Москва", 
#                            "США" : "Вашингтон",
#                            "Франция" : "Париж"}
# for country in countries_and_capitals:
#     print(f'У страны {country} столица - {countries_and_capitals[country]}')

# countries = dict()
# country = input("Введите название страны: ")
# str_number = 0
# while country != "СТОП":
#     if country not in countries:
#         countries[country] = [str_number]
#     else:
#         countries[country].append(str_number)
#     str_number += 1
#     country = input()
# for country in countries:
#     print(f'{country}: {countries[country]}')

countries = dict()
country = input("Введите название страны: ")
str_number = 0
while country != "СТОП":
    if country not in countries:
        countries[country] = [str_number]
    else:
        countries[country].append(str_number)
    str_number += 1
    country = input()
for country in countries:
    print(f'{country}: {countries[country]}')