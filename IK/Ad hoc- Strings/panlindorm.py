def palindorm(A):
    j = len(A)-1
    
    for idx in range(len(A)//2):    
        if A[idx] != A[j]:
            return False
        else:
            j -= 1
    return True
        
print(palindorm('abcdcba'))