num = [1,2,3,4]

length = len(num)
sum = 0

for i in num:
    length -= 1
    i = i *(10**length)
    sum += i
    print(i)

print(f"Result: {sum}")
