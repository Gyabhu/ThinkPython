


def validate(keys):
        def inner(*args,**kwargs):
            key = int(input("Password: "))
            if key == 1234:
                return keys(*args,**kwargs)
            print("Access denied")
        return inner
@validate
def message(*args,**kwargs):
    print("Hello World")

message(1234)