class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        return f"Это {self.name} - {self.species}"

class Mammal(Animal):
    def __init__(self, name, species, warm_blood=True):
        super().__init__(name, species)
        self.warm_blood = warm_blood
    
    def display_info(self):
        return f"Это {self.name} - {self.species}, {self.warm_blood}"

class Bird(Animal):
    def __init__(self, name, species, can_fly=True):
        super().__init__(name, species)
        self.can_fly = can_fly

    def display_info(self):
        return f"Это {self.name} - {self.species}, {self.can_fly}"
    
class Zoo():
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all_animals(self):
        for animal in self.animals:
            animal.display_info()

cow = Animal("Корова", "травоядное")
cat = Mammal("Кошка", "хищник")
eagle = Bird("Орел", "птица")