# https://fellowship.hackbrightacademy.com/materials/challenges/decode/index.html#decode

def decode(word):
    res = []
    for i, char in enumerate(word):
        # print(char)
        if char.isnumeric():
            # print(i, int(char))
            skip = int(char)
            res.append(word[skip+i+1])
    return ''.join(res)

words = ["0h", "2abh", "0h1ae2bcy"]
for word in words:
    print(decode(word))
    print('------')