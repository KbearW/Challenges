# https://leetcode.com/problems/count-and-say/

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

#     countAndSay(1) = "1"
#     countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

# To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

# For example, the saying and conversion for digit string "3322251":

# Given a positive integer n, return the nth term of the count-and-say sequence.

 

# Example 1:

# Input: n = 1
# Output: "1"
# Explanation: This is the base case.

# Example 2:

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

 

# Constraints:

#     1 <= n <= 30
class Solution:
    def countAndSay(self, n: int) -> str:
#         res = '1'
#         for i in range(n-1):
#             res = self.getnext(res)
#         return res
    
#     def getnext(self,res):
#         i, next_seq = 0, ''
#         while i<len(res):
#             count = 1
# # i< len(seq)-1--> limit the # of times this is being run..remember 0 indexing? 
#             while i< len(res)-1 and res[i] == res[i+1]:
#                 count += 1
#                 i += 1
# #Exit the while loop when two # ain't the same, nest the res once before moving back into the while loop
#             next_seq += str(count) + res[i]
#             i += 1
#         return next_seq

        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s