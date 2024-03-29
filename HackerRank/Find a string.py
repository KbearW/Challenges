# https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Constraints


# Each character in the string is an ascii character.

# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input

# ABCDCDC
# CDC

# Sample Output

# 2
def stringValidators1(s):
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))
        
if __name__ == '__main__':
    s = input()
    stringValidators1(s)    
