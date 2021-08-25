def myAtoi(s):
# strip spaces at the beginning 
    s = s.strip()
    sign = 1
    res = 0
    i = 0
    
    if not s:
        return (f'L9:{s}')
    
    try:
        if s[0] == '-':
            sign = -1
            if not s[1].isnumeric():
                return 0
    except:
        return 0

    try:
        if s[0] == '+':
            sign = 1
            if not s[1].isnumeric():
                return 0
    except:
        return 0

    for i in range(len(s)):
        if sign == 1 and i<len(s)-1 and s[0] == '+':
            if s[i+1].isnumeric() == True:
                res = res*10 + int(s[i+1])
            else:
                break
        if sign == 1 and i<len(s):
            if s[i].isnumeric() == True:
                res = res*10 + int(s[i])
            else:
                break
        if sign == -1 and i<len(s)-1:
            if s[i+1].isnumeric() == True:
                res = res*10 + int(s[i+1])
            else:
                break
            
    if sign == 1:
        if sign*res < 2**31-1:
            return sign*res
        else:
            return 2**31-1
    else:
        if sign*res > -2**31:
            return sign*res
        else:
            return -2**31
    



# myAtoi("42")
# myAtoi("   -42")
# myAtoi("4193 with words")
# myAtoi("words and 987")
# myAtoi("-91283472332")
# myAtoi("3.5465")
# myAtoi("+1")
# myAtoi("-9999999999999")
myAtoi("     +004500")