# we can use class method to make object inside a method.

# we use class methods to make factory methods

class Vehicle:
    category = 'car'
    @classmethod
    def printcategory(cls):
        print(f'Vehicle Category = {cls.category}')

Vehicle.printcategory()
my_vehicle = Vehicle()
my_vehicle.printcategory()
