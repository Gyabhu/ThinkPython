d = {"name": "Gyabs",
    "age": 21}

# looping keys in dictionary

for key in d.keys():
    print(key)

# looping values in dictionary

for value in d.values():
    print(value)

# This is same as d.keys
for i in d:
    print(i)



for g, a in d.items():      # Tuple unpacking
    print(g, a)


#Enuemurate built-in function

enew = [1,2,3,4,5]

# Tuple unpacking
for index, values in enumerate(enew, start= 1):
    print(index, values)