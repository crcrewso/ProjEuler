"""Project Euler Question 4

Question:
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
    9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers
"""


def isPalendrome(number):
    """
    Tests that a number is a palindrome by converting to a string

    :int number:
    :return: True IFF the number is a palindrome
    """
    forward = str(number)
    reverse = forward[::-1]
    if forward == reverse:
        return True
    return False


max_palendrome = 0
for i in range(1000, 0, -1):
    for j in range(i, 0, -1):
        test = i * j
        if isPalendrome(test):
            if (test > max_palendrome):
                max_palendrome = test

print(max_palendrome)
