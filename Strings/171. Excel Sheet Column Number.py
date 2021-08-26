# https://leetcode.com/problems/excel-sheet-column-number/

# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            x = ord(char)-ord('A')+1
            res = res*26+x
        return res