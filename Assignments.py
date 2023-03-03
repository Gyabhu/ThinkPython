n = int(input("Enter n: "))
new = 0
total = 0
for i in range(n):
    new = new*10+n
    total = total + new
    print(new)
print("Total is ", total)

