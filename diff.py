n = int(input("Enter n: "))

if n > 17:
    diff = (n-17)*2
    print("Since the n is greater than 17, the value is doubled ", diff)
else:
    diff = 17-n
    print("Since the n is lesser than 17, the value is exact ", diff)