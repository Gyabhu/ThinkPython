# Protected is denoted by underscore("_") before variable or method.
class Vehicle:
    def __init__(self):
        self.color = 'red'
        self._mileage = 110

    def change_mileage(self,mileage):
        self._mileage = mileage

yatri = Vehicle()

print("Before:",yatri._mileage)
yatri.change_mileage(100)
print("After:",yatri._mileage)

''' This is also possible, but not recommended'''

yatri._mileage = 80
print(yatri._mileage)