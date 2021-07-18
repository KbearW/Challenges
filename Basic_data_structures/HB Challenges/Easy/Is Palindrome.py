# https://fellowship.hackbrightacademy.com/materials/challenges/is-palindrome/index.html#is-palindrome

# Return True/False if this word is a palindrome. A palindrome is a word that is spelled the same backwards and forwards.

# >>> is_palindrome("a")
# True

# >>> is_palindrome("noon")
# True

# >>> is_palindrome("racecar")
# True

# >>> is_palindrome("porcupine")
# False

# Treat spaces and uppercase letters normally—so “Racecar” wouldn’t be a palindrome since “R” and “r” aren’t the same letter:

# >>> is_palindrome("Racecar")
# False

# We’ve included a file, ispalindrome.py with a is_palindrome method:

# def is_palindrome(word):
#     """Return True/False if this word is a palindrome."""

# However, this is unimplemented.

def is_palindrome(word):
    """Return True/False if this word is a palindrome."""
    
    # Note:
    # len of word, int(len/2) for both odd & even
    # use slides

    # Sudo:
    # find the len of the word
    # find the midpoint of the word
    # mid_point = int(len/2)
    # slice the ending and put the rev. order in a str
    # condition: 
        # slice word to see if both front and back ==
        # return 
        # 
    
    mid_point = len(word)//2

    for index in range(mid_point):

    #     # print(f'front: {word[index]}')
    #     # print(f'end: {word[-(index)-1]}')
        
        if word[index] == word[-index-1]:
            pass
        return False
    return True
