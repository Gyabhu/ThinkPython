class A:
    def display(self):
        return "This is class A."
class B:

    def display(self):
        return "This is class B"
class C(A,B):
    def display(self):
        return 'Hi, ' + A.display('')

obj = C()


print(obj.display())