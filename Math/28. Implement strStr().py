# https://leetcode.com/problems/implement-strstr

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:

# Input: haystack = "", needle = ""
# Output: 0

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # with built in function
        # return haystack.find(needle)
    
        # method #2
        # # edge cases:
        # if len(needle)==0:
        #     return 0
        # for i in range(len(haystack)):
        #     if haystack[i: i+len(needle)] == needle:
        #         return i
        # return -1
        
        # Method #3
        if len(needle)==0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
    
    # Method 2 & 3: Time complexity: O(n)
        
# two pointer approach