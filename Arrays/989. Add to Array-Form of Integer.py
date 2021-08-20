# https://leetcode.com/problems/add-to-array-form-of-integer/submissions/

# The array-form of an integer num is an array representing its digits in left to right order.

#     For example, for num = 1321, the array form is [1,3,2,1].

# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

# Example 2:

# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455

# Example 3:

# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021

# Example 4:

# Input: num = [9,9,9,9,9,9,9,9,9,9], k = 1
# Output: [1,0,0,0,0,0,0,0,0,0,0]
# Explanation: 9999999999 + 1 = 10000000000

class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:

        res = []
        newNum = 0
        # print(len(nums))
        for i in range(0,len(nums)):
            # print(nums[i])
            # print(nums[i]*(10**i))
            newNum += nums[i]*(10**(len(nums)-i-1))
        #     print({i},{newNum})
        # print({newNum})
        newNum += k
        # newNum = str(newNum)
        for char in str(newNum):
            res.append(char)
        return res
            
# declair new var res= []    
# declair new var num = 0
# interate num and convt to int
# add k to the int
# convt int to str
# iterate over the str and put into res