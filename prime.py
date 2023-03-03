n = int(input("Enter n: "))

if n > 1:

    for i in range (2, int(n/2)+1):
        if n % i == 0:
            print(f"{n} is Constant")
            break

    else:
        print(f"{n} is Prime")

else:
    print(f"{n} is neither prime nor Constant")

