# https://fellowship.hackbrightacademy.com/materials/challenges/lucky-numbers/index.html#lucky-numbers

# Goal: given int n, return a list containing n "unique" random numbers btw 1-10, inclusive.
# limit: n < 0 and n > 10
# edge case: n = 0 will return an empty list
# answer will be sorted

# def a function
# import random lib
# iterate over n times
# append the random num to a list
# remove that random num from the option of 1-10
# return a list
import random
def lucky_numbers(n):
    res = []
    num_list = [x for x in range(1,11)]
    print(num_list)
    for time in range(n):
        num = random.choice(num_list)
        # print(num)
        num_list.remove(num)
        # print(num_list)
        res.append(num)

    return sorted(res)
n = 3
print(lucky_numbers(n))