def perm(words):
    res = []
    words = [letter for letter in words]
 
    def helper(i, temp):
        if i == len(words):
            res.append(''.join(temp))
            return
 
        else:
            for j in range(i,len(words)):
                print(words)
                # swap
                words[i], words[j] = words[j], words[i]
                temp.append(words[i])
                helper(i+1, temp)
                temp.pop()
                words[j], words[i] = words[i], words[j]
 
 
    helper(0,[])
    return res
 
print(perm('abc'))

# Permutation where input is a string + swap method
# doesn't req slate bc we can directly append the word to the array res.

def perm1(words):
    res = []
    words = [letter for letter in words]
 
    def helper(i):
        if i == len(words):
            res.append(''.join(words))
            return
 
        else:
            for j in range(i,len(words)):
                # print(words)
                # swap
                words[i], words[j] = words[j], words[i]
                # temp.append(words[i])
                helper(i+1)
                # temp.pop()
                words[j], words[i] = words[i], words[j]
 
 
    helper(0)
    return res
 
print(perm1('abc'))
# ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']