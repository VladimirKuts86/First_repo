n = int(input("Введите число: "))
sum = 0
i = 1
while i <= n:
    if i % 3 == 0:
        sum += i
    i += 1    
print(sum)