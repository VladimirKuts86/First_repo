animals = ["слон", "тигр", "слон", "зебра", "тигр", "тигр", "зебра"]
Slon = animals.count("слон")
Tiger = animals.count("тигр")
Zebra = animals.count("зебра")

print(f'Слонов: {Slon}, тигров: {Tiger}, зебр: {Zebra}')

unique_animals = []
counts = []
for animal in animals:
    if animal not in unique_animals:
        unique_animals.append(animal)
        counts.append(1)
    else:
        index = unique_animals.index(animal)
        counts[index] += 1

for i in range(len(unique_animals)):
    print(f'{unique_animals[i]}: {counts[i]}')