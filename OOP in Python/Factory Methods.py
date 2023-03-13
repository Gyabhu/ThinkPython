# Example of Factory method
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def dob(cls,name,year):
        return cls(name,date.today().year - year)

    def display(self):
        print(f'{self.name} is {self.age} years old')

# Object Creation
obj = Person('Gabs',21)
obj.display()

new2 =Person.dob('Deeps',1997)
new2.display()