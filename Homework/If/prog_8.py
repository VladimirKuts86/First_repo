number = int(input("введите число: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")       
if number % 3 == 0 and not number % 5 == 0:
    print("Fizz")
if number % 5 == 0 and not number % 3 == 0:
    print("Buzz")
else:
    print(number)