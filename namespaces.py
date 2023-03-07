a = 1

def sum(b,c): # Arguement
    global a
    a = 2
    print("Inside: ", a)
    return b+c

print("Outside: ", a)
sum(19,12)  # Parameter
print("Outside: ", a)



# Types of Argument

# Positional Argument
# Default Argument
# Arbitrary Arguments

def example(a,b,c=1,*args,**kwargs)