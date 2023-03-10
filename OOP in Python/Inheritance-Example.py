class Vehicle:
    def __init__(self,brand,location):
        self.brand = brand
        self.location = location

class Seller(Vehicle):
    def __init__(self,brand,location,broker): # Method Overriding.
        self.broker = broker
        super().__init__(brand,location)




suv = Seller('Honda','Lazimpat','syakar trading')

print(suv.brand)
print(suv.location)
print(suv.broker)


