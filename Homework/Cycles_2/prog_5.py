for string in range(5):   # 5 строк
    for column in range(7):   # 7 столбцов
        if string == 0 or string == 4 or column == 0 or column == 6: # если строка 0 или строка 4 или столбец 0 или столбец 6
            print("#", end="") # печатаем решетки
        else:  # в противном случае
            print(" ", end="") # печатаем пробелы
    print() # чтобы печатало на новых строках