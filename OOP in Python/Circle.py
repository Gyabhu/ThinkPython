# Magic method, Operator Overloading
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def __add__(self, obj):  # Dunder Method
        return self.radius + obj.radius

    def __gt__(self, obj):   # The concept of Operator Loading
        return self.radius > obj.radius

    def __str__(self):
        return f'Radius of the object is {self.radius}.'

# Using Method
c1 = Circle(7)
c2 = Circle(5)
result1 = c1.__add__(c2)
print(result1)

# Using Dunder method
result2 = c1 + c2
print(result2)

# Comparing using Dunder method
result3 = c1>c2
print(result3)

# Without Using method
result = c1.radius + c2.radius
print(result)
print(c2)
