# https://www.hackerrank.com/challenges/swap-case/problem

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

#     string s: the string to modify

# Returns

#     string: the modified string

# Input Format

# A single line containing a string
# .

def swap_case(s):
    res = ''
    for char in s:
        if char.isalpha() == True:
            if char.isupper() == True:
                res += char.lower()
            if char.islower() == True:
                res += char.upper()
        else:
            res += char
    return res

    # Steps:
    # New var to store the modified stings
    # iterate over the input
        
    # check if each char is alpha
            # if char is upper case
        #         append char in lower case
        #     else: (if char is lower case)
        #         append char in upper case
    # else- not alpha
        # append 
    # return new var
    
if __name__ == '__main__':