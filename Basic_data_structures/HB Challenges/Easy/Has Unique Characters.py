# https://fellowship.hackbrightacademy.com/materials/challenges/has-unique-chars/index.html#has-unique-chars

# Given a word, return True if that word contains only unique characters. Return False otherwise.

# >>> has_unique_chars("Monday")
# True

# >>> has_unique_chars("Moonday")
# False

# >>> has_unique_chars("")
# True

# Uppercase and lowercase letters should be considered separately:

# >>> has_unique_chars("Bob")
# True

# We’ve included hasuniquechars.py, which contains the stub of a has_unique_chars function:
# hasuniquechars.py

# def has_unique_chars(word):
#     """Does word contains unique set of characters?"""

# Implement this function.

def has_unique_chars(word):
    """Does word contains unique set of characters?"""
    unique_chars = set()
    for char in word:
        unique_chars.add(char)
    if len(word) > len(unique_chars):
        return False
    else:
        return True