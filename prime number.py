a = int(input("Enter a number: "))
if a < 2:
    print("Not a Prime Number")
else:
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
