"""Project Euler Question 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

import math

for a in range(1000, 2, -1):
    for b in range(a, 1, -1):
        for c in range(1000 - a - b, 0, -1):
            if (a + b + c == 1000):
                triplet = (a * a) + (b * b)
                if triplet == c * c:
                    print(a * b * c)
