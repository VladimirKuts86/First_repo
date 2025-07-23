def resolve_tri_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника не могут быть меньше ноля!")
    if a == b and b == c:
        return "Треугольник равносторонний"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return "Прямоугольный"
    elif a==b or b==c or c==a:
        return "Равнобедренный"
    else:
        return "Разносторонний"

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    result = resolve_tri_type(a, b, c)
    print(result)
