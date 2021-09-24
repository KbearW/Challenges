# https://fellowship.hackbrightacademy.com/materials/challenges/truncate-repeats/index.html#truncate-repeats

'''input: string, output: string '''

def truncate(word):
    res = []
    
    for char in word:
        if not res or char != res[-1]:
            res.append(char)

    return ''.join(res)

word = 'aaaaabbbbcccaaaa'
print(truncate(word))