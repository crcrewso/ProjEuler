"""Project Euler Question 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
    1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""

import math

number = 1
max_divisors = 500

while True:
    triangular_number = sum(range(1, number))
    divisors = 0
    for i in range(1, triangular_number + 1):
        if (triangular_number % i) == 0:
            divisors += 1
        if (i == int(math.sqrt(triangular_number)) and divisors < (max_divisors / 2)):
            break
    if divisors >= max_divisors:
        print(number)
        print(triangular_number)
        exit()
    number += 1
