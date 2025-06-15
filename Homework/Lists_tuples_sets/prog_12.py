list_with_doubles = ['Иван', 'Анна', 'Петр', 'Анна', 'Иван']
list_of_guests = []
set_without_doubles = set()
for name in list_with_doubles:
    if name not in list_of_guests:
        list_of_guests.append(name)
        set_without_doubles.add(name)
    else:
        continue
print(set_without_doubles, list_of_guests)
