# Summation of primes
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def euler_10(n):
    total = 2
    for next_prime in get_primes(3):
        if next_prime < n:
            total += next_prime
        else:
            return total

n = 2000000
print('\nSolving Euler 10 for {:,}...'.format(n))
total = euler_10(n)
print('\nThe sum of all primes below {:,}: {:,}\n'.format(n, total))

# The sum of all primes below 2,000,000: 142,913,828,922