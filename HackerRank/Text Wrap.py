# https://www.hackerrank.com/challenges/text-wrap/problem

# You are given a string and width .
# Your task is to wrap the string into a paragraph of width

# .

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

#     string string: a long string
#     int max_width: the width to wrap to

# Returns

#     string: a single string with newline characters ('\n') where the breaks should be

# Input Format

# The first line contains a string,
# .
# The second line contains the width,

# .

# Constraints

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    
    type(textwrap.fill(string,max_width))

# use the textwrap library- .fill function to split up all char based on the max_width
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

wrap('abcdef',2)