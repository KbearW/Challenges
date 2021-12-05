def palindorm(A):
    j = len(A)-1
    
    for idx in range(len(A)//2):    
        if A[idx] != A[j]:
            return False
        else:
            j -= 1
    return True
        
# print(palindorm('abcdcba'))

def palindorm2(s):
    left = 0
    right = len(s)-1

    if left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1 
    return True
print(palindorm2('abcdcba'))
# True