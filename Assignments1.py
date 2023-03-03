# WAP that accepts an integer (n) and computes the value of n+nn+nnn+...

n = int(input("Enter the number: "))
total = 0
for i in range(1,n):
    sum = str(n)
    sum = str(n) * i
    print(sum)
    total += int(sum)
print("Total :", total)




