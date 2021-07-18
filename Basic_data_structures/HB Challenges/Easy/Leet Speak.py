# https://fellowship.hackbrightacademy.com/materials/challenges/leet-speak/index.html#leet-speak

# in which standard letters are often replaced by numerals or special characters.

# Letter
	

# Becomes

# a
	

# @

# o
	

# 0

# e
	

# 3

# l
	

# 1

# s
	

# 5

# t
	

# 7

# In this exercise, you’ll make a function that translate a word to leet-speak:

# >>> translate_leet("Hi Balloonicorn")
# 'Hi B@1100nic0rn'

# >>> translate_leet("Hackbright is the Shizzle")
# 'H@ckbrigh7 i5 7h3 5hizz13'

# We’ve given you leet.py, which includes the stub of a translate_leet function:
# leet.py

def translate_leet(phrase):
    """Translates input into "leet-speak"."""
    # Sudo:
    # setup a new var for the new string
    # setup a dict to store those values
    # iterate over the phrase and replace each char
    # return the new string

    new_string = ''
    replacement = {'a':'@',
                    'o':'0',
                    'e':'3',
                    'l':'1',
                    's':'5',
                    't':'7'}
    
    # for char in phrase:
    #     if char in replacement:
    #         new_string += replacement[char]
    #     else:
    #         new_string += char
    # print(new_string)

    for char in phrase:
        new_string += replacement.get(char,char)
    print(new_string)

    # Tips:
    # when see dict, use the relevant methods
