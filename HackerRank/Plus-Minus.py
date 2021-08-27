# https://www.hackerrank.com/challenges/plus-minus/problem

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with

# places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to

# are acceptable.

# Example
# There are elements, two positive, two negative and one zero. Their ratios are , and

# . Results are printed as:

# 0.400000
# 0.400000
# 0.200000

# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

#     int arr[n]: an array of integers

#!/bin/python3

import math
import os
import random
import re
import sys
# import collections

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    count = {'pos':0,'neg':0,'zero':0}
    length = len(arr)
    for x in arr:
        if x>0:
            count['pos'] +=1
        if x<0:
            count['neg'] += 1
        if x ==0:
            count['zero'] += 1
    
    for k,v in count.items():
        print(v/length)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
