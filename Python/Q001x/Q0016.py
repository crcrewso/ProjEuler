"""Project Euler Question 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import math

string = str(int(math.pow(2, 1000)))
sum_of_chars = 0
for char in string:
    sum_of_chars += int(char)
print(sum_of_chars)
