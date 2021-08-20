# https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

# TBD... This is complicated with an inplace solution--> O(1) space.
# What needs to happen-->
# use two pointer method to keep track of curr and zeroes (aka prev),

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
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

#     Order:
            # [0,1,0,3,12]
            # [1,0,0,3,12]
            # [1,3,0,0,12]
            # [1,3,12,0,0]
    
        
# Note:
#     two pointers, swap method

# Pseudo code:
    # iterate over the input list:
#     if num equ 0:
        # pop that elem and add that to the end of the list <-- This logic is off, don't pop it, swap it!
    # (By using pop, order of the list will be retain but indexing will be off!) <-- this is wrong
    # return list