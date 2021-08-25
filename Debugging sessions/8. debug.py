def myAtoi(s):

    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    res = 0
    i = 0
    
    if s[0] == '-':
        sign = -1
    
    if s[0].isnumeric():
        return 0
    
    for i in range(len(s)):
        if s[i].isnumeric() == True:
            res = res*10 + int(s[i])
            
    if -2*31 <sign*res < 2**31-1:
        return sign*res
    else:
        return 2**31*sign
    
    return sign * res

myAtoi("42")
myAtoi("   -42")
myAtoi("4193 with words")
myAtoi("words and 987")
myAtoi("-91283472332")