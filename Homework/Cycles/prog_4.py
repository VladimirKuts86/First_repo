n = int(input("Введите число: "))
sum = 0
for i in range(1, n+1):
    if i % 2 != 0:
        continue
    sum += i
print(sum)    
