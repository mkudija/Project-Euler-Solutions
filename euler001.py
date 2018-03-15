# Problem 1 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


n = 1000

def mul_3_or_5(number):
    if (number%3==0) or (number%5==0):
        return True

true_list = []
for i in range(1,n):
    if mul_3_or_5(i)==True:
        true_list.append(i)

print('Sum of all multiples of 3 and 5 below {}: {}'.format(n, sum(true_list)))

# Sum of all multiples of 3 and 5 below 1000: 233168