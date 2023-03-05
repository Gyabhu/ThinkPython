a =[5,9,1,3,4,9,1,6,7]
items = len(a)
for i in len(a):
    for j in range(items-i-1):
        if j > a[0]:
            sorted.append(i)

print(sorted)