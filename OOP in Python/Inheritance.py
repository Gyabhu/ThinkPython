'''

    Inheritance can be defined as a process in which methods, properties and attributes of a
    class can be inherited by another clas.


    examples of Inheritance:

        class Vehicle:
            def __init__(self,brand,location)
                self.brand = brand
                self.location = location

        class Seller(Vehicle):
            def __init__(self,brand,location,broker)
                self.broker = broker
                super().__init__(brand,color)

        truck = Vehicle('Honda','Lazimpat','syaka trading')



'''