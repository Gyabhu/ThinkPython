# Method Overloading is not possible in python.
class MethodOverLoad:
    def area (self, l):
        return l*l

    def area (self, l,b):
        return l*b

ans = MethodOverLoad()
#print(ans.area(12))

class MethodOverLoadV2:
    def area (self, l, b=None):
        if b is not None:
            return l*b
        return l*l

ans2 = MethodOverLoadV2()
print(ans2.area(5))
print(ans2.area(6,98))
