# Напишите функцию find_longest_word(*words), которая принимает любое количество строк 
# и возвращает самую длинную из них.

def find_longest_word(*words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(longest)
find_longest_word("Шла Саша", "по шоссе", "и жевала сушки")