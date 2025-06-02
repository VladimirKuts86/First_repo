brick = "*"
size = 5
while size > 0:
    print(brick * size)
    size -= 1

brick = "*"
size = 5
for i in range(size, 0, -1):
    for _ in range(i):
        print(brick, end="")
    print("")
