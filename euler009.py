# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
import time

start_time = time.time()

a = 3
b = 4
c = 5


for i in range(100):
	if a**2 + b**2 == c**2:
		print("YES")
	print('{}, {}, {}'.format(a,b,c))
	a += 1
	b += 1
	c += 1




# print('The highest product of {} adjacent numbers is: {}\n'.format(n, max(products)))

print('Execution time: {:.1} sec'.format(time.time() - start_time))


# The highest product of 13 adjacent numbers is: 23514624000

# Execution time: 0.00598 sec
