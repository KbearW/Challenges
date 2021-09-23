# https://fellowship.hackbrightacademy.com/materials/challenges/rev-string/index.html#rev-string

'''reverse the string given. cannot use reverse or reversed()'''
# case not senstitive

# iterate over the string and use slice method to rebuild a word, runtime: O(n**2), space: O(n)

def rev_string(word):
    res = ''
    for i in range(len(word)+1):
        res += word[-(i+1)]
    return res

words = ['porcupine','Abc',[]]
for word in words:
    print(rev_string(word))