'''
    Try,Except,Else,Finally
'''
 # Incomplete


def add(x,y):
    return x + y


try:
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
except ValueError:
    print('Cannot add string and int')

else :
    result = add(a,b)
    print(result)

print(divide())

