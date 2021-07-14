# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

# By this logic, we say a sequence of brackets is balanced if the following conditions are met:

#     It contains no unmatched brackets.
#     The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.

# Given

# strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

# Function Description

# Complete the function isBalanced in the editor below.

# isBalanced has the following parameter(s):

#     string s: a string of brackets

# Returns

#     string: either YES or NO

# Input Format

# The first line contains a single integer
# , the number of strings.
# Each of the next lines contains a single string

# , a sequence of brackets.

# Constraints

# , where

#     is the length of the sequence.
#     All chracters in the sequences ∈ { {, }, (, ), [, ] }.

# Output Format

# For each string, return YES or NO.

# Sample Input

# STDIN Function ----- -------- 3 n = 3 {[()]} first s = '{[()]}' {[(])} second s = '{[(])}' {{[[(())]]}} third s ='{{[[(())]]}}'

# Sample Output

# YES
# NO
# YES

# Explanation

#     The string {[()]} meets both criteria for being a balanced string.
#     The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
#     The string {{[[(())]]}} meets both criteria for being a balanced string.


import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    # sudo:
    # setup stack
    # setup dict w all brackets --> {'[':']','(':')','{':'}'}
    # loop: for char in s:
        #if char in open brackets
            #append to stack
        # if char not in open brackets--> close bracket
            # look for the last item within the stack (top) by using pop
            # find match in the dict != char
                # if true, --> 'no'
    # else--> once finished the loop
    # return 'NO' if stack is not empty and 'YES' if empty
        
    stack = []
    bracket = {'[':']','(':')','{':'}'}
    for char in s:
        if char in ['(','[','{']:
            stack.append(char)
        else:
            # if stack is not empty
            if stack:
                top = stack.pop() #top= last item in the stack
                if bracket[top] != char: #bracket[top]--> lookup the closing bracket
                    return 'NO'
            # when list == empty
            else:
                return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'
    
    # return 'NO' if stack else 'YES'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
