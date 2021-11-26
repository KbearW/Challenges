# Both BFS methods will have same result... 
# under BFS method: Runtime is O(2**n)*n and space is O(2**n)
# DFS is always better bc of O(n) space

# BFS / recursion method
def binarystringsrecursive(n):
    if n == 1:
        return ["0", "1"]
    else:
        prev = binarystringsrecursive(n-1)
        res = []
        for s in prev:
            res.append(s + "0")
            res.append(s + "1")
    return res

binarystringsrecursive(3)
# ['000', '001', '010', '011', '100', '101', '110', '111']

# BFS / iterative method
def binarystrings(n):
    res = ["0","1"]
    for item in range(1,n):
        newres = []
        for s in res:
            newres.append(s+'0')
            newres.append(s+'1')
        res[:] = newres[:]
    return res

print(binarystrings(3))
# ['000', '001', '010', '011', '100', '101', '110', '111']

# 