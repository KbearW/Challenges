# https://leetcode.com/problems/valid-palindrome/

# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers: left and right
        # Method #1 O(n) runtime | O(1) space
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()        
        
        n = len(res)    
        left = 0
        right = n-1  

        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True
    

# Note:--> return T/F if doesn't match
#     Ignore space and ,.!? + cases--> .lower() and isalnum
#     left and right pointers,
#     find the function for is alphabet/number--> .isalnum
