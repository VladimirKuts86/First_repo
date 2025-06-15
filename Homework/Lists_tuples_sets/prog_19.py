capitals = {'Россия': 'Москва', 'Франция': 'Париж', 'Италия': 'Рим'}
new_capitals = {}
for key, value in capitals.items():
    new_capitals[value] = key
print(new_capitals)