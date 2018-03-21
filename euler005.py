# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

start_time = time.time()

def divisible_by_all(number, range_top):
	total = 0
	numbers = range(1,range_top+1)
	for i in numbers:
		if number%i==0:
			total+=1
	if total==len(numbers):
		return True


range_top = 20

i = 1
while True:
	x = divisible_by_all(i, range_top)
	if x==True:
		break
	i+=1

print('The smallest number that can be evenly divided by all numbers from 1 to {} is: {}\n'.format(range_top, i))

print('Execution time: {:.3} sec'.format(time.time() - start_time))


# The smallest number that can be evenly divided by all numbers from 1 to 20 is: 232792560

# Execution time: 4.03e+02 sec