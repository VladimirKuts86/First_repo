# # 17. Создание шахматной доски из 0 и 1
matrix = ([i for i in range(2)]*4)
counter = 0
while counter < 8:
    for element in matrix:
        print(element, end="")
    counter += 1
    matrix = matrix[::-1]
    print()
                    



