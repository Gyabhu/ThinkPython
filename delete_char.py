s = "I am Groot and I love Plants"
def del_str(a):
    print("    *******I am Groot and I love Plants*******")
    i = input('Enter char to delete: ')
    # method 1
    i = i.lower()
    return a.replace(i, "")

# method 2
new = ""
for x in s:
    if x in i:
        continue
    else:
        new += x

print(new)

