# https://fellowship.hackbrightacademy.com/materials/challenges/balanced-parentheses/index.html#balanced-parentheses

# Given a string, return True or False depending on whether that string has balanced parentheses.

# For the purposes of this problem, you only need to worry about parentheses (( and )), not other opening-and-closing marks, like curly brackets, square brackets, or angle brackets.

# For example:

#  >>> has_balanced_parens("()")
#  True

#  >>> has_balanced_parens("(Oh Noes!)(")
#  False

#  >>> has_balanced_parens("((There's a bonus open paren here.)")
#  False

#  >>> has_balanced_parens(")")
#  False

#  >>> has_balanced_parens("(")
#  False

# >>> has_balanced_parens("(This has (too many closes.) ) )")
# False

# You may consider a string with no parentheses balanced:

# >>> has_balanced_parens("Hey...there are no parens here!")
# True

# We given you a file, balancedparentheses.py, with a has_balanced_parens function:
# balancedparentheses.py

# However, this function is unimplemented. Implement this function to uncover any any stray parentheses!

def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    stack = []

    for char in phrase:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False
        else:
            pass
    return True if not stack else False