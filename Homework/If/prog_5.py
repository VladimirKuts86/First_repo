year = int(input("Введите год: "))
if year % 400 == 0:
    print("Год високосный")
elif year % 4 == 0 and year % 100 != 0:
    print("Год високосный")
else:
    print("Год не високосный")