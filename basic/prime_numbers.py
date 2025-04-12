# check the prime numbers under the range of 100

prime_range = int(input("Enter the range upto which prime are to be calculated : "))

prime_nums = []

for n in range(2,prime_range):
    for x in range(2,n):
        if n%x == 0:
            break
    else:
        print(f"{n} is prime")
        prime_nums.append(n)

print(f"Prime Number between 1 and {prime_range} are {prime_nums}")

