first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
if first_number > second_number:
    print("Первое число больше")
else:
    print("Второе число больше")

# Задача 2

Number = float(input("Введите число "))
if Number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

# Задача 3

Number = int(input("Введите число "))
if Number == 0:
    print("Число равно нолю")
elif Number < 0:
    print("Число отрицательное")
else:
    print("Число положительное")

# Задача 4

number_1 = float(input("Ведите первое число "))
number_2 = float(input("Ведите второе число "))
operations = input("Введите оперцию ")
if operations == "+":
    plus = number_1 + number_2
    print(plus)
if operations == "-":
    minus = number_1 - number_2
    print(minus)
if operations == "*":
    umnozhit = number_1 * number_2
    print(umnozhit)
if operations == "/":
    if number_2 == 0:
        print("На ноль делить нельзя, введите корректное число")
    else:
        razdelit = number_1 / number_2
        print(razdelit)            


# Задача 5

year = float(input("Введите год: "))
if year % 400 == 0:
    print("Год високосный")
elif year % 4 == 0 and year % 100 == >0<:
    print("Год високосный")
else:
    print("Год не високосный")

