# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math
import time

start_time = time.time()

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


n = 10001

primes = [2]
i = 3
while True:
	if is_prime(i)==True:
		primes.append(i)
		if len(primes)==n:
			break
	i+=1


print('The {}st prime number is: {}\n'.format(n, primes[-1]))

print('Execution time: {:.3} sec'.format(time.time() - start_time))


# The 10001st prime number is: 104743

# Execution time: 0.126 sec