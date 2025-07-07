# Напишите функцию is_in_range(number, min_val, max_val), которая возвращает True,
# если число number находится в диапазоне 
# от min_val до max_val (включительно), и False в противном случае.

def is_in_range(number, min_val, max_val):
    if number not in range(min_val, max_val+1):
        return False
    return True
print(is_in_range(int(input()), int(input()), int(input())))