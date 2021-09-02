# https://www.hackerrank.com/challenges/capitalize/problem

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

# Given a full name, your task is to capitalize the name appropriately.

# Input Format

# A single line of input containing the full name,

# .

# Constraints

#     The string consists of alphanumeric characters and spaces.

# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# Output Format

# Print the capitalized string,

# .

# Sample Input

# chris alan

# Sample Output

# Chris Alan

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(' ')
    res = []
    for word in s: 
        res.append(word.capitalize())
    return ' '.join(res)
    
    # steps:
    # split input s
    # return cap of the 1st char of each word and append to res
    # in this case, it's better not set res as string bc it's hard to conv to plain strings later w a space in btw
    
if __name__ == '__main__':
   