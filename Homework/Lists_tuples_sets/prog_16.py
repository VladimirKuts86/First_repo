strings_list = ['Маша', 'Петя', 'Вася', 'Маша', 'Петя', 'Маша']
strings_dict = {}
for name in strings_list:
    if name not in strings_dict:
        strings_dict[name] = 1
    elif name in strings_dict:
        strings_dict[name] += 1
print(strings_dict)
    