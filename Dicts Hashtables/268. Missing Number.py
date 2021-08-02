# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# Example 4:

# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

class Solution:
    def missingNumber(self, inputlist: List[int]) -> int:

        list1 = [num for num in range(0,len(inputlist)+1)]
        for num in list1:
            if num not in inputlist:
                return num
            
#             Runtime here is O(n^2)

        n = len(nums)
        return int(n*(n+1)/2 - sum(nums))

        # Runtime is O(n) & space complexity is O(1)

# didn't say have to solve it as a string! can do it w math way!

# Note:
#     n is not given
#     n starts at 0... aka len is correct, range(0,n+1)

# Pesudo Code:
# find max num
# print out the num list- inclusive of 0 and n --> range (0,n+1)
# check if x in numlist
#     if not, return the num

# Can simplfy it to two lines
# check if x not in range(0,len+1):
#     return x