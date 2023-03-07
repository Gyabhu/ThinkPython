<<<<<<< HEAD
a = [5,9,1,3,4,9,1,6,7]
items = len(a)
sorted()
for i in a:
=======
list =[7,9,4,2]
items = len(list)
for i in range(items):
>>>>>>> 8799250491c238cd0c4bd350c9d0f35dd5ad575c
    for j in range(items-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list)