#~~~~~~~~~~~ With repetitions --> ie. Binary / Decimal strings ~~~~~~~~~~~~~~~~~

# All DFS will have runtime = O(2**n)n  and space = O(n), always recursive
# DFS will perform most work upfront. (unlike BFS- which perfom most of the work at the very end.)

# This method will return a list of all items
# subfunction can assess variable in the global scope

# recursive method
def binarystrings(n):
    res = []
    def bshelper(slate,n):
        if n == 0:
            res.append(slate)
        else:
            bshelper(slate + '0', n-1)
            bshelper(slate + '1', n-1)
    bshelper("", n)
    return res

binarystrings(3)
# ['000', '001', '010', '011', '100', '101', '110', '111']

def binarystrings(n):
    res = []
    def bshelper(slate,n):
        if n == 0:
            res.append(slate)
        else:
            bshelper(slate + '0', n-1)
            bshelper(slate + '1', n-1)
    bshelper("", n)
    return res

binarystrings(3)
# ['000', '001', '010', '011', '100', '101', '110', '111']

# This is flexible and can run thu a range... slight modification
def binarystrings_int(n):
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
binarystrings_int(2)
# ['00', '01', '10', '11', '20', '21']

def binarystrings_str(n):
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
binarystrings_str(arr)
# ['aa', 'ab', 'ba', 'bb']


#~~~~~~~~~~~ Without repetitions ~~~~~~~~~~~~~~~~~
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
