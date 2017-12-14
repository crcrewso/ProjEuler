"""Project Euler Question 5

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

### makes a first guess

max_int = 20

number = 1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
number = number - (number % max_int)

while True:
    divided_by_all_in_range = True
    for i in range(2, max_int):
        if number % i != 0:
            divided_by_all_in_range = False
            break
    if divided_by_all_in_range:
        print(number)
        exit()

    number += max_int  # since the number has to end in 0, this incriments by 0's
