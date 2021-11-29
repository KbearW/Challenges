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
permutations_wo_repetitions_str(['abc'])
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# Best space--> set temp/ slate as array and join since string is immutable and array is mutable.
def permutations_wo_repetitions_str(n):
    res = []
    def bshelper(slate,n):
        if len(n) == 0:
            res.append(''.join(slate))
        else:
            for i in range(len(n)):
                arr2 =  n[:i] + n[i+1:]
                print(arr2)
                bshelper(slate + str(n[i]), arr2)
                # bshelper(slate + '1', n-1)
    bshelper([], n)
    print(res)
    return res
permutations_wo_repetitions_str(['abc'])
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

''' This is the best solution for the classic permutation problem: instead of slicing the string, swap it to save space!'''
def perm(words):
    res = []
    # This step is to split letters into individual string for easy access later
    
    words = [char for char in words]
    
    def helper(i, words, temp):
        # Base case:
        if len(words) == i:
            res.append(''.join(temp))
            return
        
        # Inner node
        else:
            for j in range(i, len(words)):
                # swap with current string... in this example, when i = 1, words = 'bac' rather than 'abc'
                words[i], words[j] = words[j], words[i]
                # same logic here... append curr char to temp and pop it out when done
                temp.append(words[i])
                helper(i+1, words, temp)
                temp.pop()
                # swap back to original
                words[j], words[i] = words[i], words[j]
            
    helper(0,words,[])
    return res
print(perm('abc'))
# ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']