class Vehicle:
    category = 'car'

    def __init__(self,color,doors):  # Constructor creation
        self.color = color
        self.doors = doors

    def description(self):
        return(f"This is vehicle is a {Vehicle.category} painted in {prado.color} and it has {prado.doors} doors ")

    def make_it_purple(self):
        self.color = 'purple'


#Object creation
prado = Vehicle('red','8')
rolls = Vehicle('green',4)
tesla = Vehicle('black',4)


print(f"vehicle category is {prado. __class__.category}") # userdeined Constructor
print(f"vehicle color is {prado.color}")
print(f"vehicle has {prado.doors} doors")
print(f"vehicle category is {Vehicle.category}")  #used default constructor
print(f"After {prado.color}")
