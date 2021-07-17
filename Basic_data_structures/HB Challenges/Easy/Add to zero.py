# https://fellowship.hackbrightacademy.com/materials/challenges/add-to-zero/index.html#add-to-zero
# Given list of ints, return True if any two nums in list sum to 0.

# >>> add_to_zero([])
# False

# >>> add_to_zero([1])
# False

# >>> add_to_zero([1, 2, 3])
# False

# >>> add_to_zero([1, 2, 3, -2])
# True

# Given the wording of our problem, a zero in the list will always make this true, since “any two numbers” could include that same zero for both numbers, and they sum to zero:

# >>> add_to_zero([0, 1, 2])
# True

# We’ve given you addtozero.py, which has an add_to_zero function:
# addtozero.py

# def add_to_zero(nums):
#     """Given list of ints, return True if any two nums sum to 0."""

# This function isn’t implemented, though, so when we run addtozero.py, we have test failures.

def add_to_zero(nums):
    if len(nums)>1:
        for i in range(len(nums)):
            for j in range(1,len(nums[1:])+1):
                sum = nums[i] + nums[j]
                # print(f'num[i]: {nums[i]}')
                # print(f'nums[j]: {nums[j]}')
                if sum == 0:
                    # print('True')
                    return True
                else:
                    return False
    else:
        # print('False')
        return False