number_1 = int(input("Введите первое число: "))
operation = input("Введите операцию:")
number_2 = int(input("Введите второе число: "))
if operation == "+":
    print("Результат сложения:", number_1 + number_2)
elif operation == "-":
    print("Результат вычетания:", number_1 - number_2)
elif operation == "*":
    print("Результат умножения:", number_1 * number_2)
else:
    while number_2 == 0:
        number_2 == int(input("На ноль делить нельзя!\nВведите корректное число (не 0):"))
    if number_2 != 0:
        print("Результат деления:", number_1 / number_2)
