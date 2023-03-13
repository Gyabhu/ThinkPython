'''
    Try,Except,Else,Finally
'''
 # Incomplete


def add(x,y):
    return x + y
a = input("Enter Number: ")
b = input("Enter Number: ")

try:
    add(a+b)

except ValueError:
    print('Cannot add string and int')

else :
    add(str(a) + str(b))

