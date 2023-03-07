
a = [1,2,1,1,2,3,4,4,5]

def repeated(list):
    b = []
    for i in a:
        if a.count(i) > 1 and i not in b:
            b.append(i)

    print(b)

repeated(a)