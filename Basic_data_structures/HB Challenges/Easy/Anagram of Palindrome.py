# https://fellowship.hackbrightacademy.com/materials/challenges/anagram-of-palindrome/index.html#anagram-of-palindrome

# # pesudocode
def is_anagram_of_palindrome(word):
    # try #1
#     # new var stack as array
#     stack = []
#     # sort input
#     wordsorted = sorted(word)
#     # iterate over the input
#     i = 0
#     while i<len(wordsorted):
#         for i, char in enumerate(word):
#         # append char to stack
#             stack.append(char)
#             print(stack)
#         #     if next char equals to last elem in stack
#             if char[i] == stack[-1]:
#                 stack.pop()
#             print(stack)
#     #         remove the item from stack
#     if len(stack) > 1:
#     # if length of stack is greater than 1
#         return False
#     #     return False
#     return True
    # else return true 

    # Try #2
    # iterate over input
    map = {}
    for char in word:
    # put items in k,v dict pair
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1
    
    res = 0
    for count in map.values():
        if count == 1:
            res += 1
    # print(res)
    if res >1:
        return False
    else:
        return True
        # return False
    # find the length of v that is 1
    # if the result is more than 1 key, 
    #     return False
    # else:
    #     return True

print(is_anagram_of_palindrome('arceace'))
print(is_anagram_of_palindrome("arceaceb"))