year = float(input("Введите год: "))
if year % 400 == 0:
    print("Год високосный")
if year % 4 == 0 and not year % 100 == 0:
    print("Год високосный")
else:
    print("Год не високосный")