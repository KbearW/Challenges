# https://fellowship.hackbrightacademy.com/materials/challenges/largest-smaller-than/index.html#largest-smaller-than

# Given an ordered list of numbers and a number, return the index of the largest number in the list that is smaller than that number.

# For example:

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 10)
# 2

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 33)
# 4

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -1)
# 1

# Never find xnumber — it’s not smaller than itself!

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], 8)
# 1

# If no such number exists, return None:

# >>> find_largest_smaller_than([-5, -2, 8, 12, 32], -10) is None
# True

# We’ve given you a stub function. Implement it:
# largest_smaller_than.py

def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""
    
    num_list = []

    if nums[0] >= xnumber:
        print(None)

    for num in nums:
        if num < xnumber:
            num_list.append(num)
    
    if len(num_list)>0:
        print(len(num_list)-1)
    


# Tips
# deal w the edge cases first- fail fast to save runtime!