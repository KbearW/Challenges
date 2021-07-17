# https://fellowship.hackbrightacademy.com/materials/challenges/find-range/index.html#find-range

# Given a list of numbers, return the smallest and the largest number.

# >>> find_range([3, 4, 2, 5, 10])
# (2, 10)

# >>> find_range([43, 3, 44, 20, 2, 1, 100])
# (1, 100)

# For an empty list, it should return None as both smallest and largest:

# >>> find_range([])
# (None, None)

# Make sure it works with a list of one item, which is both smallest and largest:

# >>> find_range([7])
# (7, 7)

# We’ve given you range.py, which includes the stub of a find_range function:
# range.py

# def find_range(nums):
#     """Given list of numbers, return smallest & largest number as a tuple."""

def find_range(nums):
    if len(nums) == 0:
        print([None,None])
    else:
        minval = nums[0]
        maxval = nums[0]
        for num in nums:
            if num>maxval:
                maxval = num
            if num<minval:
                minval = num
        # maxval = max(nums)
        # minval = min(nums)
        print ((minval, maxval))
