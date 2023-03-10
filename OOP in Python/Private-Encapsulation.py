# Denoted by double underscore ("__") before any methods or variable


class Vehicle:
    def __init__(self):
        self.color = 'red'
        self._mileage = 110
        self.__topspd = '90km/hr'


yatri = Vehicle()

'''Accessing private properties, this is also called "Name Mangling" '''

print(yatri._Vehicle__topspd)