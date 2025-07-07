# Напишите функцию join_with_separator(str1, str2, separator), 
# которая объединяет две строки через указанный разделитель.

def join_with_separator(str1, str2, separator):
    return str1 + separator + str2
print(join_with_separator("ABC", "HHP", " & "))