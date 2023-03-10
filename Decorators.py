# def add(a,b):
#     return a+b
#
# print(add(5,5))

import time
def decorator(function):
    def inner_function(*a,**b):
        start = time.time()
        result = function(*a,**b)
        end = time.time() - start
        print("Time taken ", end)
        return result
    return inner_function
@decorator
def add(a,b,c,d,e):
    return a + b + c + d + e


print(add(10,20,43,2345234,23533))
#add = decorator(add)


# import time
# start = time.time()
# print(add(10,15))
# end = time.time()-start
#
# print(f"The total time is ", end)




