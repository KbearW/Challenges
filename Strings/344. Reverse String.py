# https://leetcode.com/problems/reverse-string/

# Write a function that reverses a string. The input string is given as an array of characters s.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # print(s[::-1])
        s.reverse()
        
        
# Note:
# reversed() or [::-1] to reverse a string --> missing .reverse()
# do not return anything.... modify s in place