numb = int(input("Введите число: "))
for i in range(1, 11):
    five = numb * i % 5
    print(numb, "*", i, "=", (numb * i))
    if five == 0:
        print("Фу, 5 опять....")
  