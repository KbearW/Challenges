# https://fellowship.hackbrightacademy.com/materials/challenges/days-in-month/index.html#days-in-month

# Goal: return the # of days in that month

# def function
# return num_of_days
# setup day_counts for month in two lists exp for feb
# figure out if it's a leap year
# if leap and feb
# return 29 days
# return days

def helper(year):
    '''Helper function for leap year'''
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    '''return the number of days given month and year'''
    month = int(date.split()[0])
    year = int(date.split()[1])
    day_count_31 = [1, 3, 5, 7, 8, 10, 12]
    day_count_30 = [4, 6, 9, 11]
    day = 0

    if month in day_count_31:
        day = 31
    if month in day_count_30:
        day = 30
    if month ==2:
        if helper(year) == True:
            day = 29
        else:
            day = 28

    print(day)

date = "02 2015"
days_in_month(date)