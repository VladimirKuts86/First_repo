figure = input("Введите фигуру (круг, прямоугольник, треугольник): ")
if figure == "круг":
    radius = float(input("Введите радиус круга: "))
    square = 3.14 * radius ** 2
    print(square)
elif figure == "прямоугольник":
    width = float(input("Введите ширину прямоугольника: "))
    length = float(input("Введите длину прямоугольника: "))
    square = width * length
    print(square)
elif figure == "треугольник":
    height = float(input("Введите высоту треугольника: "))
    side = float(input("Введите сторону треугольника: "))
    square = 1/2 * side * height
    print(square)