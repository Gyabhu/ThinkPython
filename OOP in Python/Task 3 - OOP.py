class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_details(self):
        return f'Hi, I am {self.name} and I am {self.age} years old.'

class Employee(Person):

    def __init__(self,name,age,salary,designation):
        self.salary = salary
        self.designation = designation
        super().__init__(name,age)

    def get_details(self,obj):
        print(super().get_details())
        return f'My salary is Rs.{self.salary} and I work as an {self.designation}.'


e1 = Employee('Gabs',22,'450,000','SWE')
print(e1.get_details())

