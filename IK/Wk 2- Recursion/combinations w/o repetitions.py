def binarystrings(n):
    res = ["0","1"]
    for item in range(2,n):
        newres = []
        for s in res:
            newres.append(s+'0')
            newres.append(s+'1')
        res[:] = newres[:]
    return res
    

print(binarystrings(3))
# ['00', '01', '10', '11']