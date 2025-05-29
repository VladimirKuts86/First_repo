numb = int(input("Введите число: "))
sum = numb
while numb != 0:
    numb = int(input("Число не является нолём. Введите ноль: "))
    sum += numb
if numb == 0:
    print("Вы ввели правильное число. Спасибо!")
    if sum != 0:
        print("Сумма всех введёных чисел: ", sum)