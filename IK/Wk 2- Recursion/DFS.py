#~~~~~~~~~~~ With repetitions --> ie. Binary / Decimal strings ~~~~~~~~~~~~~~~~~
'''
All DFS will have runtime = O(2**n)n  and space = O(n), always recursive
DFS will perform most work upfront. (unlike BFS- which perfom most of the work at the very end.)

This method will return a list of all items
subfunction can assess variable in the global scope

Note: when the result asks to be a 2D array, slate/ temp needs to be an array as the inner unit.
Otherwise, it will fail the test cases.

'''
# recursive method
# For int

def binaryint(n):
    res = []
    def bshelper(slate,n):
        if n == 0:
            res.append(slate)
        else:
            bshelper(slate + '0', n-1)
            bshelper(slate + '1', n-1)
    bshelper("", n)
    return res

binaryint(3)
# ['000', '001', '010', '011', '100', '101', '110', '111']

'''_________________________________________________________________'''
# For int

# This is flexible and can run thu a range... slight modification
def binaryint2(n):
    res = []
    def bshelper(slate,n):
        if n == 0:
            res.append(slate)
        else:
            for i in range(n+1):
                bshelper(slate + str(i), n-1)
                # bshelper(slate + '1', n-1)
    bshelper("", n)
    print(res)
    return res
binaryint2(2)
# ['00', '01', '10', '11', '20', '21']

'''_________________________________________________________________'''
# For strings

def binarystrings(n):
    res = []
    # Make a copy of the input for referrence
    input = n[:]
    # print(input)
    def bshelper(slate,n):
        if len(n) == 0:
            res.append(slate)
        else:
            # in this for loop, it needs to ref back to the input arr
            for i in range(len(input)):
                # because n need to be n-1 going fwd
                bshelper(slate + input[i], n[1:])
                # bshelper(slate + '1', n-1)
    bshelper("", n)
    # print(res)
    return res

arr = ['a','b']
binarystrings(arr)
# ['aa', 'ab', 'ba', 'bb']

'''_________________________________________________________________'''

#~~~~~~~~~~~ Without repetitions ~~~~~~~~~~~~~~~~~
# For int:

def binarystrings_wo_repetitions_int(n):
    res = []
    def bshelper(slate,n):
        if n == 0:
            res.append(slate)
        else:
            for i in range(n):
                arr2 =  n - 1
                print(arr2)
                bshelper(slate + str(i), arr2)
                # bshelper(slate + '1', n-1)
    bshelper("", n)
    print(res)
    return res
binarystrings_wo_repetitions_int(2)
# ['00', '10']

def binarystrings_wo_repetitions_int2(n):
    res = []
    def bshelper(slate,n):
        if n == 0:
            res.append(slate)
        else:
            for i in range(n):
                slate += [n[i]]
                arr2 =  n - 1
                print(arr2)
                bshelper(slate + str(i), arr2)
                slate.pop()
                # bshelper(slate + '1', n-1)
    bshelper([], n)
    print(res)
    return res
binarystrings_wo_repetitions_int2(2)
# [['00'], ['10']]


'''_________________________________________________________________'''
# For Strings

def permutations_wo_repetitions_str(n):
    res = []
    def bshelper(slate,n):
        if len(n) == 0:
            res.append(slate)
        else:
            for i in range(len(n)):
                arr2 =  n[:i] + n[i+1:]
                print(arr2)
                bshelper(slate + str(n[i]), arr2)
                # bshelper(slate + '1', n-1)
    bshelper("", n)
    print(res)
    return res
permutations_wo_repetitions_str(['a','b','c'])
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
