n = int(input("Ведите число: "))
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        sum += 1
print("Всего чётных чисел было: ", sum)