# https://fellowship.hackbrightacademy.com/materials/challenges/days-in-month/index.html#days-in-month

# Given a string with a month and a year (separated by a space), return the number of days in that month.

# Leap years are a bit tricky. A year is a leap year if and only if:

#     it is evenly divisible by 4

#     except if it is divisible by 100, in which case it isn’t

#     except if it is divisible by 400, in which case it is

# So, for example, 1904 was a leap year. 1900 is divisible by 100, so it wasn’t. 2000 is divisible by 400, so it was.

# To help with this, we’ve given you a function to determine if a year is a leap year; you may use this in your solution:
# daysinmonth.py

# def is_leap_year(year):
#     """Is this year a leap year?

#     Every 4 years is a leap year::

#         >>> is_leap_year(1904)
#         True

#     Except every hundred years::

#         >>> is_leap_year(1900)
#         False

#     Except-except every 400::

#         >>> is_leap_year(2000)
#         True
#     """

#     if year % 400 == 0:
#         return True

#     if year % 100 == 0:
#         return False

#     if year % 4 == 0:
#         return True

# The Input

# The month will be given as a number.

# >>> for i in range(1, 13):
# ...     date = str(i) + " 2016"
# ...     print "%s has %s days." % (date, days_in_month(date))
# 1 2016 has 31 days.
# 2 2016 has 29 days.
# 3 2016 has 31 days.
# 4 2016 has 30 days.
# 5 2016 has 31 days.
# 6 2016 has 30 days.
# 7 2016 has 31 days.
# 8 2016 has 31 days.
# 9 2016 has 30 days.
# 10 2016 has 31 days.
# 11 2016 has 30 days.
# 12 2016 has 31 days.

# >>> days_in_month("02 2015")
# 28

# We’ve given you daysinmonth.py, which has a days_in_month function:
# daysinmonth.py

# def days_in_month(date):
#     """How many days are there in a month?"""

# This function isn’t implemented, though, so when we run daysinmonth.py, our doctests fail. Complete this function so that the doctests pass.
