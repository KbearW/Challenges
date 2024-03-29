# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for num, count in count.items():
            # print(num, count)
            if count == 1:
                return num
# Ask: O(n) runtime, memory: only an extra one
# Pesudo code:
# iterate over the nums input
# len= odd/even--> invalid

        # Method #2- O(1)--> XOR --> 0*0 = 0 |1*1 = 0, b/c of this property, when iterating, can easily spot the leftover. If unclear, watch a video on XOR.
        
        values = 0
        for num in nums:
            values ^= num
        
        return values