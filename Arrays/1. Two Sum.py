# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate (nums):
            k = target - num
            if k in seen: #--> O(1)
                return [seen[k],i]
            else:
                seen[num] = i
            
# Runtime is O(n)

# Note:
# Only one answers, len of nums list is at least 2
# 2 steps:
# find the num within array that adds to targe
# convt the num to index and display in a list

# Pesudo Code:
# Method #1--> O(n^2)--> brute force method
# nested loop
# if target-nums[n] in nums
# iterate over the list
# n = len(nums)+1
    # for i in range(0,n):
        # for j in range(1,n):
            # if target - nums[i] == nums[j]:
                # return [i,j]


# Method #2--> O(n)
# recursive method / hashmap method
# Base case: if match, return index
# else(itself)


# issue:
# what to do with this example
# Input: [3,2,4]
# 6
# Output: [0,0]
# Expected: [1,2]
# Stdout: {3: 0, 2: 1, 4: 2}

# Solution: find ways to not use range(1,len(nums))