# # https://leetcode.com/problems/valid-parentheses/

# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# # An input string is valid if:

# #     Open brackets must be closed by the same type of brackets.
# #     Open brackets must be closed in the correct order.

 

# # Example 1:

# # Input: s = "()"
# # Output: true

# # Example 2:

# # Input: s = "()[]{}"
# # Output: true

# # Example 3:

# # Input: s = "(]"
# # Output: false

# # Example 4:

# # Input: s = "([)]"
# # Output: false

# # Example 5:

# # Input: s = "{[]}"
# # Output: true


# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Sudo:
#         # new var --> Stack = []
#         # paren= {'[':']','{':'}','(':')'} --paren pairs
#         # loop thru s(input):
#             # if char in ['(','[','{']: open parens
#                 # add to Stack
#             # else: --> must be either a closing paren or empty list
#                 # if not empty: --> must be a closing paren  (think of edge cases--> when it doesnt match the paren pair, return 'false)
#                     # if Stacks[-1] == char:
#                         # Stacks.pop()
#                     # else:
#                         # return 'false
#                 # else:
#                     # return false

#         stack = []
#         paren = {'[':']','{':'}','(':')'}
#         for char in s:
#             if char in ['(','[','{']: 
#                 stack.append(char)
#                 # print(f'{stack}')
#             else:
#                 if stack:  #if list is truthy--> not empty
#                     if paren[stack[-1]] == char:  #peek
#                         stack.pop()

#                     else:
#                         return False
#                 else:
#                     return False
#         #if the final stack is empty--> return True else False
#         return False if stack else True 



def isValid(s):
#     brackets={')':'(','}':'{',']':'['}
#     stack = []
#     for char in s:
#         if char in brackets.values():
#             stack.append(char)
#         elif char in brackets.keys():
#             if stack == [] or brackets[char] != stack.pop():  
#                 return False
#         else:
#             return False
#     return stack == []
# isValid('{[})')
        
        # What's the diff btw above and below? above doesn't work but below do.
        #     def isValid(self, s):
#         stack = []
#         dict = {"]":"[", "}":"{", ")":"("}
#         for char in s:
#             if char in dict.values():
#                 stack.append(char)
#             elif char in dict.keys():
#                 if stack == [] or dict[char] != stack.pop():
#                     return False
#             else:
#                 return False
#         return stack == []
        
# Pesudo code:
# setup dict, stack = []
# iterate over the input 
# condition: if char in "(","{","[")
# add to stack
# else:
#     if char[i] == stack
#     .pop()
# if stack: return false
# else: return true