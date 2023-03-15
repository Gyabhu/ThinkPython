'''

        Defination:

        using keyword 'open' > filename

'''

# file = open("python.txt",'w')
# file.write("This is python and definilty not from amazon forest")
# file.close()

file = open("python.txt",'r')
print(file.read())

# Today's Practice for memory leakage prevention

with open("python.txt",'r'):
    print(file.read())