# assert условие, "Сообщение об ошибке"

def division(a, b):
    assert b != 0, "На ноль делить нельзя"
    return a/b
print(division(10, 0))