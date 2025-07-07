# Напишите функцию find_in_slice(data, element, start, end), которая
# ищет element в списке data только в срезе от start до end (не включая end).
# Если элемент найден, функция должна вернуть его индекс в исходном списке, иначе — -1.

def find_in_slice(data, element, start, end):
    for number in data:
        if number != element in range(start, end):
            return print(-1)
        else:
            return data.index(element)

print(find_in_slice([10, 5, 8, 12, 85], 12, 0, 3))