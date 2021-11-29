# This starts the fill from the left of the array.
# Note this uses mutable data structure by setting temp as an [] rather than a '', this helps to improve the space.
# B/c we can skip creating new string each time.
# Time: O(2**n) <=> O(brench)**height
# Space: O(n) <=> O(height)
# DFS

def function(array):
    res = []
    
    def helper(i, temp, array):
        # base case
        if len(temp) == len(array):
            res.append(''.join(temp))
            print(f"line 8:{''.join(temp)[::-1]}")
            # print(res)
            return
        else:
            if array[i].isdigit():
                temp.append(array[i])
                # print(''.join(temp))
                helper(i+1, temp, array)
                temp.pop()
            else:
                temp.append(array[i].lower())
                # print(temp)
                helper(i+1, temp, array)
                temp.pop()
                
                temp.append(array[i].upper())
                # print(temp)
                helper(i+1, temp, array)
                temp.pop()
        
    helper(0, [], array)
    return res
print(function('a1b2'))
# ['a1b2', 'a1B2', 'A1b2', 'A1B2']


# This starts the fill from the right of the array.
def function(array):
    res = []
    
    def helper(i, temp, array):
        # base case
        if len(temp) == len(array):
            res.append(''.join(temp)[::-1])
            print(f"line 8:{''.join(temp)[::-1]}")
            # print(res)
            return
        else:
            if array[i].isdigit():
                temp.append(array[i])
                # print(''.join(temp))
                helper(i-1, temp, array)
                temp.pop()
            else:
                temp.append(array[i].lower())
                # print(temp)
                helper(i-1, temp, array)
                temp.pop()
                
                temp.append(array[i].upper())
                # print(temp)
                helper(i-1, temp, array)
                temp.pop()
        
    helper(len(array)-1, [], array)
    return res
print(function('a1b2'))
# ['a1b2', 'a1B2', 'A1b2', 'A1B2']