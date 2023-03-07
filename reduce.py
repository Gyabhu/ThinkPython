from functools import reduce


def addition_bro(a,b):
    return a + b

c = [1,2,3,4,5,6,7,8,9]
result = reduce(addition_bro, c)
lambda_result = reduce(lambda x,y: x+y , c)
print(result)
print(lambda_result)
