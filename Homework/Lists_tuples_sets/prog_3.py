Animals = ["лев", "зебра", "тигр", "жираф", "волк", "слон"]
Predators = ["лев", "тигр", "волк"]
number_of_predators = 0
number_of_herbivores = 0
for i in Animals:
    if i in Predators:
        number_of_predators += 1
    else:
        number_of_herbivores += 1
print(f"Хищников: {number_of_predators}, травоядных: {number_of_herbivores}")