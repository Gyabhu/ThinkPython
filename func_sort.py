list =[7,9,4,2]

def sorted(a):
    items = len(list)
    for i in range(items):
        for j in range(items-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    print(a)

sorted(list)