number_1 = float(input("Ведите первое число "))
operations = input("Введите оперцию ")
number_2 = float(input("Ведите второе число "))
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
