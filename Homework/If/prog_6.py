hour = int(input("Введите сколько сейчас часов (0-23): "))
if 6 <= hour <= 11:
    print("Сейчас утро")
elif 12 <= hour <= 17:
    print("Сейчас день")
elif 18 <= hour <= 23:
    print("Сейчас вечер")
elif 0 <= hour <= 5:
    print("Сейчас ночь")
else:
    print("Ошибка: введите число от 0 до 23")
