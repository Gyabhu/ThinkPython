def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("syntax error")

try:
    c = int(input("A:"))
    d = int(input("A:"))

except ValueError:
    print("Enter correct info.")

else:
    result = divide(c,d)
    print(result)

print(divide(c,d))