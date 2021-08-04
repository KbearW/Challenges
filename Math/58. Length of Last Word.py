# https://leetcode.com/problems/length-of-last-word/

# Given a string s consists of some words separated by some number of spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5

# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4

# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
        
        
        
#Note:
# Look for: the length of the last word within the string
# random spaces everywhere--> mid string and end of string
# return a number

# Pesudo Code:
# split(' ')
# .strip()
# len(s[-1])