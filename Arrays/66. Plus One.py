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
        # Method #1
        # ans = []
        # sum = 0
        # result = []
        # for i, num in enumerate (digits): 
        #     ans.append(num*10**(len(digits)-i-1))
        # for num in ans:
        #     sum += num
        # sum += 1
        # strnum = (str(sum))
        # for char in strnum:
        #     result.append(char)
        # return result
        
    # Runtime: O(n)
        # Method #2
        dig_len = len(digits)
        for i in reversed(range(dig_len)):
            digits[i] += 1
            if digits[i] < 10:  #range(0,9)
                print(digits[i])
                return digits
            else:  #99  |  90  |  00--> will loop thur twice for #99 then add 1 at the beginning
                digits[i] = 0
        #100
        # if digits[0] == 0:
        digits.insert(0,1)
        print(digits)
        return digits
# Note:
# when last dig is 9, there will be an overflow.. how to deal w it
# Make sure you understand the Q and though about all the edge cases before start!
# All nums are +, int
# num in list is int
# return whole num + 1 by digits


# Pesudo code:
# try 1: .join method--> can't be done bc .join method only takes str
# try 2: iterate over the input and put in a string, then conv. it to int then +1
