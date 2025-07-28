# number = int(input())
# numbers = []
# for i in range(1, number +1):
#     if i == 0:
#         continue
#     else:
#         numbers.append(i)
# print(numbers)

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if ((x1 + 1 == x2 or x1 - 1 == x2) and (y1 + 2 == y2 or y1 - 2 == y2)) or ((x1 + 2 == x2 or x1 - 2 == x2) and (y1 + 1 == y2 or y1 - 1 == y2)):
#     print("YES")
# else:
#     print("NO")



numb = int(input())
counter = 0

if numb / 25 >= 1:
        x = int(numb / 25)
        counter += x
        numb -= x * 25
if numb / 10 >= 1:
        x = int(numb / 10)
        counter += x
        numb -= x * 10
if numb / 5 >= 1:
        x = int(numb / 5)
        counter += x
        numb -= x * 5
if numb / 1 >= 1:
        x = int(numb / 1)
        counter += x
        numb -= x * 1
print(counter)