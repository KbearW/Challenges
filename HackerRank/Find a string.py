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

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        # print(string[i:i+len(sub_string )])
        # print(string[i])
        if string[i:].startswith(sub_string):
            count += 1
            # print(string[i:])
    return count 

    # steps:
    # iterate over the string
    # for each string that starts from the ith item:
    #     check if it matches sub_string
    #         count ++
    # return count 

    
if __name__ == '__main__':