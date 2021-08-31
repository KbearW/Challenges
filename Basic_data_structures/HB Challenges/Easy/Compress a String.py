# https://fellowship.hackbrightacademy.com/materials/challenges/compress-string/index.html#compress-string

def compstring(words):
    # goal: return the shortest length of words
    res = []
    curr = ''
    count = 1
    # append the 1st item to 'res'
    curr += words[0]
    # iterate over words   

    # index error
    for i, word in enumerate(words):
    # if first char equals to next
        if i < len(word):
            if word == words[i+1]:
                count += 1
        # increase count
        # else, carry over count to 'res'
            else:
                res += str(count)
        # keep looping until the end of words
        # compare the length of res and words
    print(len(res), len(words))
    # return (min(len(res), min(len(words))))
    # return the shortest length of word string

print(compstring('aabbaabb'))