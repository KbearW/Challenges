# https://fellowship.hackbrightacademy.com/materials/challenges/balanced-parentheses/index.html#balanced-parentheses

'''given a string, return T/F if balanced parentheses'''
# edge case 1: if no parentheses
# if only opening/ closing --> False
# if ((())) --> True
# if uneven --> False
# if matching --> True

def has_balanced_parens(phrase):
    # Method #1- failed attempt
        # # if '()' not in string:
        # if '()' not in phrase:
        #     return False
        
        # stack = []
        # # iterate over the string
        # for char in phrase:
        #     if char == '(':
        #         stack.append('(')
                
        #     if char == ')' and stack[-1] == '(':
        #         stack.pop()
        # if stack:
        #     return False
    count = 0
    for char in phrase:
        if char == '(':
            count += 1
        if char == ')':
            count -= 1
            if count <0:
                return False

    if count == 0:
        return True
    else:
        return False
    
phrases = ['()', "(Oh Noes!)(", "((There's a bonus open paren here.)", ")", "(", "(This has (too many closes.) ) )"]
for phrase in phrases:
    print(has_balanced_parens(phrase))