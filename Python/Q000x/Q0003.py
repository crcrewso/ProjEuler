"""Project Euler Question 3

Question:
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
"""

import math

number = 13195  # example number
number = 600851475143
# i only have to check through the square root of the number of interest
limit = int(math.sqrt(number)) + 1
max_prime_factor = 0

primes = []
factors = []

for i in range(2, limit):
    isPrime = True
    for j in primes:
        if (i % j) == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)

for i in reversed(primes):
    if (number % i) == 0:
        max_prime_factor = i
        break
print(max_prime_factor)
