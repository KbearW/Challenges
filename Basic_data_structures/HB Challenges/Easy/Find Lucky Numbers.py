# https://fellowship.hackbrightacademy.com/materials/challenges/lucky-numbers/index.html#lucky-numbers

# Given an integer n, return a list containing n unique random numbers between 1-10, inclusive. (That is, do not repeat any numbers in the returned list.)

# You can trust that this function will never be called with n < 0 or n > 10.

# For example:

# >>> lucky_numbers(2)
# [3, 7]

# It’s legal to ask for no numbers:

# >>> lucky_numbers(0)
# []

# And if we ask for all numbers, we shouldn’t get any repeats:

# >>> sorted(lucky_numbers(10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# We’ve included a file, luckynumbers.py, with a function, lucky_numbers:

import random
def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    # Sudo:
        # Notes:
        # import random bc unique random btw 1-10 inclusive --> range(1,11)
        # use set bc it said no repeats--> result = [set()]
        # n = # of element within the list --> iternate over the range for n elements
        # return a list
    # result = set()
    # iterate over the range(1,11) nth times and use the randint function
        # append to result
    # return [result] (in a list form)


    # result = set()
    # if n>1:
    #     ele = randint(1,11)
    #     result.add(ele)
    # result1 = [result]
    # print(result1)

    # What am i missing: 
    # 1. need to repeat it nth times
    # 2. the result needs to be in a list.. not a set within the list

    list1 = [range(1,11)]
    result = []
    count = 0

    # Don't need the following section bc .remove already did the trick
    # if n == 10:
    #     result = [x for x in range(1,11)]
    #     print(result)

    while count<n:
        ele = random.choice(list1)
        list1.remove(ele)
        result.append(ele)
        count+=1
    print(result)
   

#    or
#     nums = list(range(1, 11))
#     lucky_nums = []

#     for i in range(n):
#         num = random.choice(nums)
#         nums.remove(num)
#         lucky_nums.append(num)

#     return lucky_nums
    # What am i missing: 
    # 1. need to repeat it nth times--> while loop
    # 2. the result needs to be in a list.. not a set within the list
    # maybe change it to list

    # Don't need to use randint--> use random.choice() to pick element within the list