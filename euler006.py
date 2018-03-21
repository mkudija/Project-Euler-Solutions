# Sum square difference
# Problem 6 
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time

start_time = time.time()

n = 100

def sum_of_square(n):
	sum_of_square = 0
	for i in range(1,n+1):
		sum_of_square += i**2
	return sum_of_square


def square_of_sum(n):
	sums = sum(range(1,n+1))
	square_of_sum = sums**2
	return square_of_sum

difference = square_of_sum(n) - sum_of_square(n)

print('The difference between difference between the sum of the squares of the first {} natural numbers and the square of the sum is: {}\n'.format(n, difference))

print('Execution time: {:.3} sec'.format(time.time() - start_time))


# The difference between difference between the sum of the squares of the first 100 natural numbers and the square of the sum is: 25164150

# Execution time: 0.000107 sec