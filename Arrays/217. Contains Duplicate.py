# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        # print(counter.values())
        for num, count in counter.items():
            # print(num, count)
            if count >= 2:
                return True
        return False
    
# Pseudo Code:
#     use collections.Counter built in function to put all items in a dicts
#     then iterate over the dicts.items() and only take what's needed