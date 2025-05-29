string = input("Введите строку: ")
sum = 0
for i in string:
    if i == "а":
        sum += 1
print("Количество символов а в строке: ", sum)