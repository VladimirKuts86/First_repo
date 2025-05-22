date = int(input("Введите сколько сейчас часов: "))
if 6 <= date <= 11:
    print("Сейчас утро")
if 12 <= date <= 17:
    print("Сейчас день")
if 18 <= date <= 23:
    print("Сейчас вечер")
if 0 <= date <= 5:
    print("Сейчас ночь")
