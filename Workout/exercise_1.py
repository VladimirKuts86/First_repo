import random

def guessing_game():
    number = random.randint(10, 30)
    count = 1
    while True:
        answer = int(input("Каковы ваши предположения?"))
        if count == 3:
            print("Вы исчерпали количество попыток")
            break
        elif answer == number:
            print(f"То, что нужно")
            break
        elif answer < number:
            print(f"Число {answer} слишком маленькое")
        else:
            print(f"Число {answer} слишком большое")
        count += 1
        
guessing_game()     
        
