def subsets(arr):
    res = []
    def helper(i, temp, S):
        # base case
        print(f'temp is: {temp}, temp.len: {len(temp)}, i is {i}')
        # print(i)
        if len(arr) == i:
            res.append(''.join(temp))
            return
        # inner node
        else:
            # incl
            helper(i+1, temp, S[i+1:])
            # excl
            temp.append(arr[i])
            helper(i+1, temp, S[i+1:])
            temp.pop()
            
    helper(0,[''], arr)
    return res
    
print(subsets('ab'))
# res = ['', 'b', 'a', 'ab']