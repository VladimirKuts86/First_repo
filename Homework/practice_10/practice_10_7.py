# Напишите функцию power(base, exponent=2), которая возводит число base в степень exponent.
#  По умолчанию степень равна 2 (возведение в квадрат).

def power(base, exponent=2):
    return base ** exponent

print(power(int(input())))
