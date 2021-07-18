# https://fellowship.hackbrightacademy.com/materials/challenges/max-of-three/index.html#max-of-three

# Define a function max_of_three that takes in three numbers as arguments and returns the largest of them.

# For example:

# >>> maxofthree(1, 5, 2)
# 5

# >>> maxofthree(10, 1, 11)
# 11

# We’ve given you a skeleton in maxofthree.py:

# def max_of_three(num1, num2, num3):
#     """Returns the largest of three integers"""

def maxofthree(num1, num2, num3):
    """Returns the largest of three integers"""
    max = num1

    if max < num2:
        max = num2
    else:  #max > num2
        if max < num3:
            max = num3
    
    print(max)