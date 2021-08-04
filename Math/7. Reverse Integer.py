# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21

# Example 4:

# Input: x = 0
# Output: 0

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        result = int(str(abs(x))[::-1])*sign
        if -2**31 < result < (2**31) -1:
            return result
        else:
            return 0
        
    
        
           

# Note:
# built in function: reversed or [::-1]
# result needs to be int
# there's a given range for 32-bit integer--> meaning?

# Pesudo code:
    # ask- int at the end, 
    # issue- only str can be reverse
