# https://fellowship.hackbrightacademy.com/materials/challenges/balanced-brackets/index.html#balanced-brackets

# Given a string, return True or False depending on whether the string’s opening-and-closing marks (that is, brackets) are balanced. Account for the following bracket types:

# Type
	

# Opener
	

# Closer

# Parentheses
	

# (
	

# )

# Curly Braces
	

# {
	

# }

# Square Brackets
	

# [
	

# ]

# Angle Brackets
	

# <
	

# >

# The string doesn’t need to have all four types of brackets, but if an open bracket appears, the pair should also be closed correctly.

# Many of the same test cases from our Balanced Parentheses problem apply to this expanded problem, with the caveat that they must check all types of brackets.

# These are fine:

# >>> has_balanced_brackets("<ok>")
# True

# >>> has_balanced_brackets("<[ok]>")
# True

# >>> has_balanced_brackets("<[{(yay)}]>")
# True

# These are invalid, since they have too many open brackets:

# >>> has_balanced_brackets("(Oops!){")
# False

# >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
# False

# These are invalid, as they close brackets that weren’t open:

# >>> has_balanced_brackets(">")
# False

# >>> has_balanced_brackets("(This has {too many} ) closers. )")
# False

# Here’s a case where the number of brackets opened matches the number closed, but in the wrong order:

# >>> has_balanced_brackets("<{Not Ok>}")
# False

# If you receive a string with no brackets, consider it balanced:

# >>> has_balanced_brackets("No brackets here!")
# True

# We’ve given you a file called balancedbrackets.py, which contains a has_balanced_brackets function:
# balancedbrackets.py

# However, this function is unimplemented. Implement it to uncover any pesky extra brackets!

def has_balanced_brackets(phrase):
    """Does a string have balanced parentheses?"""

    open_parens = ['{','[','(','<']
    close_parens = ['}',']',')','>']
    stack = []

    for char in phrase:
        if char in open_parens:
            stack.append(char)
        elif char in close_parens:
            if stack[-1]== char:
                stack.pop()
            else:
                return False
        else:
            pass
    return True if not stack else False