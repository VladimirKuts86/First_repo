strings = ["Hello", "", "Data", "Science", "", "Python"]
strings_length = [len(x) for x in strings if len(x) > 0]
print(strings_length)