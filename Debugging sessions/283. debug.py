# https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    prev = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            hold = nums[prev]
            nums[prev] = nums[i]
            nums[i] = hold
            prev += 1
    print(nums)

moveZeroes([0,1,0,3,12]) 