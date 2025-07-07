# Напишите функцию smart_join(separator, *items), которая объединяет все items в одну строку,
#  используя separator между ними. Первый аргумент — обязательный.
# Используйте функцию высшего порядка внутри функции (подсказка)

def smart_join(separator, *items):
    return separator.join(items)


print(smart_join(" ", "Шла Саша", "по шоссе", "и жевала сушки"))


def smart_join(separator, *items):
    return separator.join(map(str, items))


print(smart_join(" ", 55, "лет", "бывает только", "раз в жизни"))