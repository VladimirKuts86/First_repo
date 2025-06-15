list_of_tuples = [('Анна', 92), ('Борис', 88), ('Виктор', 95)]
current = 0
heighst = 0
name_best = ""
for i in list_of_tuples:
    current = i[1]
    if current > heighst:
        heighst = current
        name_best = i[0]
print(name_best)