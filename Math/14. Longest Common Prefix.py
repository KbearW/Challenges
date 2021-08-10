# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
#         strs = ["flower","flow","flight"]
        shortest = min(strs,key=len)  # "flow"
        
        for i, ch in enumerate(shortest):  #0, f | 1, l | 2, o | 3, w
            for other in strs:  #"flower","flow","flight"
                if other[i] != ch:  #f != f
                    return shortest[:i] 
        return shortest         

# Note:
#     profix only
#     iterate over the list
#     KMP Substring search
    
# code:
#     start w the min len word, reduce the char as it iterate
#     .substring