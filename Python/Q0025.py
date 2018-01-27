""" Project Euler Question 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Used a lot of math tricks

"""

import math

fibold = 1.
fibnew = 1.

fibindex = 2  # index of fibnew

print()

digits = 1

while (digits < 1000):
    temp = fibnew + fibold
    fibold = fibnew
    fibnew = temp
    fibindex += 1
    if fibnew >= 10:  # keep removing last digit every time it goes above 10 so that the number doesn't get bigger than we need
        fibold /= 10
        fibnew /= 10
        digits += 1
print(fibindex)
