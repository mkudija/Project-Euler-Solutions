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


def euler_10():
    total = 2
    for next_prime in get_primes(3):
        n = 2000000
        if next_prime < n:
            total += next_prime
        else:
            print('\nSum of Primes < {:,}: {:,}\n'.format(n, total))
            return


# for i in range(10):
#     print('{} is prime: {}'.format(i,is_prime(i)))


print('\nSolving Euler 10...')
euler_10()