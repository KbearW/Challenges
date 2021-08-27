def function(s):
    # res = ''
    # while len(s)>len(res):
    #     for i, char in enumerate(s):
    #         if s[i] != s[i+1]:
    #             res += s[i]
    #             print(res)
    # if not res:
    #     return 'Empty String'
    # return res

    stack = []
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        return 'Empty String'
    return ''.join(stack)
    
print(function('aaabccddd'))