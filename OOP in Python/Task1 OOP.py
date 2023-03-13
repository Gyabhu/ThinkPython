class Department():
    def __init__(self,name,no):
        self.name = name
        self.no = no

    def totalstu(self,*args):
        result = [i.number]
        return self.no + result

d1 = Department('Science',45)
d2 = Department('Management',60)
d3 = Department('Science',45)
d4 = Department('Management',60)
d5 = Department('Science',45)
d6 = Department('Management',60)

print(Department.totalstu(d1,d2,d3,d4,d5,d6))