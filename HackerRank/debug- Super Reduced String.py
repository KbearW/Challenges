def function(s):
    res = ''
    while len(s)<len(res)+1:
        for i, char in enumerate(s):
            if s[i] != s[i+1]:
                res += s[i]
                print(res)
    if not res:
        return 'Empty String'
    return res

function('aaabccddd')