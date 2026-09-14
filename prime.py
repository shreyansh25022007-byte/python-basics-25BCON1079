# Check whether a user-provided integer is prime.

n = int(input("Enter an integer: "))

if n < 2:
    print(f"{n} is not prime.")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")
