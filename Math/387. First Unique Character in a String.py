# https://leetcode.com/problems/first-unique-character-in-a-string/

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0

# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# Example 3:

# Input: s = "aabb"
# Output: -1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
            
        return -1
            
# Note:
#     Goal:
#         return the index of the first unique char within the string
#             if doesn't exist--> -1
# Pesudo code:
#     iterate over the string w enumerate 
#         add to dict w index
    
# runtime: O(n)

Method #2
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