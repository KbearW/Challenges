def subsets(arr):
    # for subsets- we are returning diff length of the input, that's why we HAVE to use temp/ slate
    res = []
    def helper(i, temp):
        # base case
        if len(arr) == i:
            res.append(''.join(temp))
            return

        # inner node
        else:
            # excl
            helper(i+1, temp)

            # incl
            temp.append(arr[i])
            helper(i+1, temp)
            temp.pop()
            
    helper(0,[''])
    return res
    
print(subsets('ab'))
# res = ['', 'b', 'a', 'ab']
