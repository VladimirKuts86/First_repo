list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
summa_1 = list_of_lists[0][0] + list_of_lists[1][1] + list_of_lists[2][2]
summa_2 = list_of_lists[2][2] +list_of_lists[1][1] + list_of_lists[0][0]
print(f"Сумма главной диагонали: {summa_1}. Сумма побочной диагонали: {summa_2}")