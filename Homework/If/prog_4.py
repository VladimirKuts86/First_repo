number_1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
number_2 = float(input("Введите второе число: "))

if operation == "+":
    print("Результат:", number_1 + number_2)
elif operation == "-":
    print("Результат:", number_1 - number_2)
elif operation == "*":
    print("Результат:", number_1 * number_2)
elif operation == "/":
    if number_2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        print("Результат:", number_1 / number_2)
else:
    print("Неизвестная операция. Пожалуйста, введите +, -, * или /")