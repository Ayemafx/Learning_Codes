# Python3 program to display Prime numbers till N

# function to check if a given number is prime
def isPrime(n):
    # since 0 and 1 is not prime return false.
    if n == 1 or n == 0:
        return False

    # Run a loop from 2 to n-1
    for i in range(2, n):
        # if the number is divisible by i, then n is not a prime number.
        if n % i == 0:
            return False

    # otherwise, n is prime number.
    return True


n = int(input('Enter a positive integer'))
for j in range(1, n + 1):
    # check if current number is prime
    if isPrime(j):
        print(j, end=" ")