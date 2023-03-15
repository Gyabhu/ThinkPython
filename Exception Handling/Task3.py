student = {
    "id": 1,
    "name": 'gabs',
    "age": 21,
    "department": 'BCA'
}


n = input('Enter the info you want to access: ')

try:
    print(f"The {n} of student is",student[n])

except KeyError:
    print("The key does not exist")
    print("Try these keywords: id, name, age, department")


