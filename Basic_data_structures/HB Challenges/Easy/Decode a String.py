# https://fellowship.hackbrightacademy.com/materials/challenges/decode/index.html#decode

# In this challenge, you’ll write a decoder.

# A valid code is a sequence of numbers and letters, always starting with a number and ending with letter(s).

# Each number tells you how many characters to skip before finding a good letter. After each good letter should come the next next number.

# For example, the string “hey” could be encoded by “0h1ae2bcy”. This means “skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

# A single letter should work:

# >>> decode("0h")
# 'h'

# >>> decode("2abh")
# 'h'

# Longer patterns should work:

# >>> decode("0h1ae2bcy")
# 'hey'

# We’ve provided a file, decode.py, with a stub function in it:

# def decode(s):
#     """Decode a string."""

# Implement this.

# def decode(s):
#     res = ''
#     i = 0

#     while i<len(s):
#         num_to_skip = int(s[i])
#         i += num_to_skip +1
#         res += s[i]
#         i += 1
#     return res

    # for char in s:
    #     if char.isnumeric == True:
    #         res.append(s[char])
                
    # print(res)

# decode("0h1ae2bcy")

# split based on num?


# res = ''
# iterate over the input
#     if char is number  
#         convert char to int/ num
#             take skipval and add 1
#             append letter at location in string where skipval is located
# return res 

def decode(s): 
    res = ''
    for i, char in enumerate(s):
        if char.isnumeric() == True:
            skipval = int(char) + 1
            res += (s[i + skipval])
    return res

print(decode('0h1ae2bcy'))
