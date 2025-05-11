n = int(input("Enter till where you want to check prime numbers : \n"))

for i in range(2,n):
    for r in range(2,i):
        if i%r == 0:
            print(f"{i} is not prime")
            break
    else:
        print(f"{i} is prime")


    