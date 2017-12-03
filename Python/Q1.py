"""Project Euler Question 1

Question:
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

""" built this for troubleshooting """


def isTrue(i):
    """
        A writeThrough function produced only for troubleshooting
    Args:
        :param i: The input integer

    Returns:
        :return:
    """
    # print(i)
    return i


sum = 0
for i in range(1, 1000):
    if (i % 15) == 0:
        sum += isTrue(i)
    elif (i % 5) == 0:
        sum += isTrue(i)
    elif (i % 3) == 0:
        sum += isTrue(i)
print(sum)
