operations = input()
if operations != "+" or "-" or "*" or "/":
    print("Неизвестная операция. Пожалуйста введите +, -, *, /")
    operations = input("Введите операцию (+, -, *, /): ")
else:
    print(operations)