words_list = ["камень", "лягушка", "вода", "тыква", "лягушка"]
count = 0
for i in words_list:
    if i == "лягушка":
        words_list[count] = "принц"
    elif i == "тыква":
        words_list[count] = "карета"
    count += 1
print(words_list)
