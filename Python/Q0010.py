"""Project Euler Question 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

primes = []
number = 2
while (number < 2000000):
    isPrime = True
    for j in primes:
        if (number % j) == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(number)
    number += 1

print(sum(primes))
