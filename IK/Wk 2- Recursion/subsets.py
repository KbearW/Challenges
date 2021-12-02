def subsets(arr):
    res = []
    def helper(i, temp):
        # base case
        if len(arr) == i:
            res.append(''.join(temp))
            return

        # inner node
        else:
            # incl
            helper(i+1, temp)

            # excl
            temp.append(arr[i])
            helper(i+1, temp)
            temp.pop()
            
    helper(0,[''])
    return res
    
print(subsets('ab'))
# res = ['', 'b', 'a', 'ab']