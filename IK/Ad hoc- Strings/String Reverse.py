# Immutable vs Mutable

# If string is immutable:
# use temp to store strings

def reversestring_immutable(string):
    res = ''
    n = len(string)
    # range(start, stop, step) **Exclusive of the last item--> [n-1, n-2, n-3,...0]
    for idx in range(n-1,-1,-1):
        print(idx)
        res += string[idx]
    return res
print(reversestring_immutable('abc'))
# 'cba'

# If Mutable:
# swap in place

def reversestring_immutable(string):
    
    def helper(i):
        
        n = len(string)
        for i in range(n//2):
            # swap:
            string[i], string[n-1-i] = string[n-1-i], string[i]
        
        return ''.join(string)
            
    return helper(0)
print(reversestring_immutable(['a','b','c','d']))
# 'dcba'

# Note the diff on input list btw the code above and below! One is an array, one is a string. 
# For the one w string, should split it back into an array before the code can swap assignment

def reversestring_immutable(string):
    string = [letter for letter in string]
    print(string)
    def helper(i):
        
        n = len(string)
        for i in range(n//2):
            print(i)
            # swap:
            string[i], string[n-1-i] = string[n-1-i], string[i]
        
        return ''.join(string)
            
    return helper(0)
print(reversestring_immutable('abcd'))