https://fellowship.hackbrightacademy.com/materials/challenges/anagram-of-palindrome/index.html#anagram-of-palindrome

# pesudocode
def is_anagram_of_palindrome(word):
    # new var stack as array
    stack = []
    # sort input
    word.sort()
    # iterate over the input
    for i, char in enumerate(word):
    # append char to stack
        stack.append(char)
    #     if next char equals to last elem in stack
        if char == stack[-1]:
            stack.pop()
    #         remove the item from stack
    if len(stack) > 1:
    # if length of stack is greater than 1
        return False
    #     return False
    return True
    # else return true 