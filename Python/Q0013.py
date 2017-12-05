"""Project Euler Question 13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
Saved in Q0013.txt

"""


numbers = []
f = open("Q0013.txt", 'r')
for line in f:
    numbers.append(int(line))

sum = 0.0

for num in numbers:
    sum += num

while sum > 10000000000:
    sum /= 10

print(str(int(sum)))
