# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
#         Method #1
#         count_S = collections.Counter(s)
#         count_T = collections.Counter(t)
#         if count_S == count_T:
#             return True
#         else:
#             return False

# Note: Can you do it without the build in function?
    # Method #2
    def isAnagram(self, s: str, t: str) -> bool:
        def helper(lst):
            finaldict = {}
            for char in lst:
                if char in finaldict:
                    finaldict[char] += 1
                else:
                    finaldict[char] = 1
            return finaldict
        
        if helper(s) == helper(t):
            return True
        else:
            return False
        
# Method #1: Runtime: O(n)
# Method #2: Runtime: O(n)