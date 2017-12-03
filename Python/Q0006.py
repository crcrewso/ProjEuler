"""Project Euler Question 6

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum
is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

nat_num = []
nat_num_squared = []

for i in range(1, 101):
    nat_num.append(i)
    nat_num_squared.append(i * i)

sum_squared = sum(nat_num)
sum_squared *= sum_squared  # square of the sum of the natural numbers

sum_squares = sum(nat_num_squared)

print(str(sum_squared - sum_squares))
