# print(";".join(str(1/x) for x in range(int(input()), int(input())+1)))

# interval = range(int(input()), int(input())+1)

# if 0 in interval:
#     print("Диапазон содержит 0")
# else:
#     print(";".join(str(1/x) for x in interval))


# start = input()
# end = input()

# if not (start.lstrip("-").isdigit() and end.lstrip("-").isdigit()):
#     print("Необходимо ввести два числа")
# else:
#     interval = range(int(start), int(end)+1)
#     if 0 in interval:
#         print("Диапазон содержит 0")
#     else:
#         print(";".join(str(1/x) for x in interval))


# try:
#     print(1 / int(input()))
# except ZeroDivisionError:
#     print("Ошибка деления на 0")
# except ValueError:
#     print("Невозможно преобразовать строку в число")
# except Exception:
#     print("Неизвестная ошибка")

# try:
#     print(1 / int(input()))
# except ZeroDivisionError:
#     print("Ошибка деления на 0")
# except ValueError:
#     print("Невозможно преобразовать строку в число")
# except Exception:
#     print("Неизвестная ошибка")
# else:
#     print("Операция выполнена успешно!")
# finally:
#     print("Программа завершена")

# start = input()
# end = input()

# if not (start.lstrip("-").isdigit() and end.lstrip("-").isdigit()):
#     print("Необходимо ввести два числа")
# else:
#     interval = range(int(start), int(end)+1)
#     if 0 in interval:
#         print("Диапазон содержит 0")
#     else:
#         print(";".join(str(1/x) for x in interval))


# x = int(input())
# if x < 0:
#     raise ValueError("Число должно быть положительным")

# class NumbersError(Exception):
#     pass

# class EvenError(NumbersError):
#     pass

# class NegativeError(NumbersError):
#     pass

# def no_even(numbers):
#     if all(x % 2 != 0 for x in numbers):
#         return True
#     raise EvenError("В списке не должно быть четных чисел")

# def no_negative(numbers):
#     if all(x >= 0 for x in numbers):
#         return True
#     raise NegativeError("В списке не должно быть отрицательных чисел")

# def main():
#     print("Ввведите числа в одну строку через пробюел")
#     try:
#         numbers = [int(x) for x in input().split()]
#         if no_negative(numbers) and no_even(numbers):
#             print(f'Сумма чисел равна: {sum(numbers)}')
#     except NumbersError as e:
#         print(f'Произошла ошибка: {e}')
#     except Exception as e:
#         print(f'Произошла неизвестная ошибка: {e}')

# if __name__ == "__main__":
#     main()


# if __name__ == "__main__":
#     main()


# import example_module

# example_module.some_function()


# from example_module import some_function, ExampleClass

# some_function()


