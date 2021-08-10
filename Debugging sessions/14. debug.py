def longestCommonPrefix(strs):
    
#         strs = ["flower","flow","flight"]
    shortest = min(strs,key=len)  # "flow"
    
    for i, ch in enumerate(shortest):  #0, f | 1, l | 2, o | 3, w
        for other in strs:  #"flower","flow","flight"
            if other[i] != ch:  #f != f
                return shortest[:i] 
    return shortest 

longestCommonPrefix(["flower","f","flight"])