number_1 = float(input("Ведите первое число "))
operations = input("Введите оперцию ")
number_2 = float(input("Ведите второе число "))
if operations != "+" or "-" or "*" or "/":
    print("Неизвестная операция. Пожалуйста введите +, -, *, /")
    operations = input("Введите операцию (+, -, *, /): ")
if operations == "+":
    print("Зезультат: ", number_1 + number_2)
elif operations == "-":
    print("Результат: ", number_1 - number_2)
elif operations == "*":
    print("Результат: ", number_1 * number_2)
elif operations == "/":
    if number_2 == 0:
        print("На ноль делить нельзя, введите корректное число")
        number_2 = float(input("Ведите второе число "))
    else:
        print("Результат: ", number_1 / number_2)