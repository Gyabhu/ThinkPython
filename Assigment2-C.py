# WAP to combine 2 dictionaries by adding their values for common keys.

d1 = {'a':100, 'b':200, 'c':300, 'd':400}
d2 = {'a':300, 'b':200, 'e':300, 'f':400}


def dict_combine(a,b):
    d = dict()
    for i in a:
        d[i] = a[i]
        if i in b:
            d[i] += b[i]
    for i in b:
        if i not in d:
            d[i] = b[i]
    print(d)

dict_combine(d1, d2)


