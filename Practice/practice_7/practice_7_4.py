list_of_strings = ["42", "100", "abc", "Nan", "7"]
numbers_in_list = [int(x) for x in list_of_strings if x.isnumeric()]
print(numbers_in_list)