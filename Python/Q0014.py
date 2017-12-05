"""Project Euler Question 13

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def collatz(num):
    if num % 2 == 0:
        return num/2
    else:
        return 3*num + 1


max_reps = 0
largest_num_seed = 0
for i in range(1, 1000000, 2):
    reps = 0
    number_of_interest = i
    while number_of_interest > 1:
        number_of_interest = collatz(number_of_interest)
        reps += 1
    if (reps > max_reps):
        max_reps = reps
        largest_num_seed = i

print(largest_num_seed)