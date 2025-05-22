figure = input("Введите фигуру (круг, прямоугольник, треугольник): ")
if figure == "круг":
    radius = int(input("Введите радиус круга: "))
    square = 3.14 * radius ** 2
    print(square)
elif figure == "прямоугольник":
    width = int(input("Введите ширину прямоугольника: "))
    length = int(input("Введите длину прямоугольника: "))
    square = width * length
    print(square)
elif figure == "треугольник":
    height = int(input("Введите высоту треугольника: "))
    side = int(input("Введите сторону треугольника: "))
    square = 1/2 * side * height
    print(square)