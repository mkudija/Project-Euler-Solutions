# Largest prime factor
# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

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


# n = 600851475143
n = 600851475143
i = 1
factors = []

while i < n/2:
	if (n%i==0) and (is_prime(i)==True):
		factors.append(i)
		print('\t{}'.format(i))
		fact2 = n/i
		if is_prime(fact2)==True:
			factors.append(fact2)
			print('\t{}'.format(fact2))
			i = fact2
	i+=1

print('The largest prime factor of {}: {}'.format(n, int(max(factors))))

print('Execution time: {:.3} sec'.format(time.time() - start_time))

# NOTE: 6857 is the correct answer but I need a faster algorithm! 