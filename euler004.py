# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number):
    """Returns TRUE if number is a palindrome"""
    nString = str(number)
    if nString==nString[::-1]:
        return True

palindromes = []
for i in range(1000):
    for j in range(1000):
        if is_palindrome(i*j):
            palindromes.append(i*j)

print('Maximum palindrome of product of 3-digit numbers is:  {}'.format(max(palindromes)))

# Maximum palindrome of product of 3-digit numbers is:  906609