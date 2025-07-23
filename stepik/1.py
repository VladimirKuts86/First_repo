# number = int(input())
# numbers = []
# for i in range(1, number +1):
#     if i == 0:
#         continue
#     else:
#         numbers.append(i)
# print(numbers)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x1 + 1 == x2 or x1 - 1 == x2) and (y1 + 2 == y2 or y1 - 2 == y2)) or ((x1 + 2 == x2 or x1 - 2 == x2) and (y1 + 1 == y2 or y1 - 1 == y2)):
    print("YES")
else:
    print("NO")
