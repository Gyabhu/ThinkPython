
# function in python are called first-class citizen
#     function are objects
#     function can be store in data structure
#     function can be passed as a parameter in another function
#     function can be nested
def func(name):
    return "Hello " + name.upper() + "."
def greet(my_func):
    messages = my_func('jane')
    print(messages)

greet(func)


# Closure
def hello(msg):
    def printmsg():
        print(msg)
    return printmsg

message = hello('Hello world 2023!')
message()