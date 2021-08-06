# https://leetcode.com/problems/plus-one/

# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# Example 3:

# Input: digits = [0]
# Output: [1]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ans = []
        sum = 0
        result = []
        for i, num in enumerate (digits): 
            ans.append(num*10**(len(digits)-i-1))
        for num in ans:
            sum += num
        sum += 1
        strnum = (str(sum))
        for char in strnum:
            result.append(char)
        return result
        
    # Runtime: O(n)
    
# Note:
# Make sure you understand the Q and though about all the edge cases before start!
# All nums are +, int
# num in list is int
# return whole num + 1 by digits


# Pesudo code:
# try 1: .join method--> can't be done bc .join method only takes str
# try 2: iterate over the input and put in a string, then conv. it to int then +1
