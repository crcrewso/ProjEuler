"""Project Euler Question 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1901
day = 0
month = 0
sundayIsFirsts = 0
while year < 2001:
    month = 0
    while month < 12:
        daysInMonth = months[month]
        if year % 4 == 0 and month == 2:
            daysInMonth += 1
        if day == 0:
            sundayIsFirsts += 1
        day = day + daysInMonth
        day = day % 7
        month += 1
    year += 1
print(sundayIsFirsts)
