# class Rocket():

#     def __init__(self):
#         self.x = 0
#         self.y = 0

#     def move_up(self):
#         self.y += 1

# my_rocket = Rocket()
# print('Rocket altitude:', my_rocket.y)
# my_rocket.move_up()
# print('Rocket altitude:', my_rocket.y)
# my_rocket.move_up()
# print('Rocket altitude:', my_rocket.y)

# my_rockets = []

# for x in range(0, 5):
#     new_rocket = Rocket()
#     my_rockets.append(new_rocket)

# my_rockets = [Rocket() for _ in range(0, 5)]

# my_rockets[0].move_up()
# for rocket in my_rockets:
#     print("Rocket altitude: ", rocket.y)
   

# class Rocket():

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def move_up(self):
#         self.y += 1

# rockets = []
# rockets.append(Rocket())
# rockets.append(Rocket(0,10))
# rockets.append(Rocket(100, 0))

# for index, rocket in enumerate(rockets):
#     print(f'Rocket {index} is at {rocket.x, rocket.y}')


class Rocket():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.y += y_increment
        self.x += x_increment

my_rockets = [Rocket() for _ in range(0, 3)]
my_rockets[0].move_rocket()
my_rockets[1].move_rocket(10, 10)
my_rockets[2].move_rocket(-10, 0)


for index, rocket in enumerate(my_rockets):
    print(f'Rocket {index} is at {rocket.x, rocket.y}')