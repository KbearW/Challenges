# https://fellowship.hackbrightacademy.com/materials/challenges/encipher-string/index.html#encipher-string

# case senstitive, take in # and string

# .isalpha()

def cipher(phrase, shift):
    alpha = 'abcdefghijklmopqrstuvwxyz'
    res = []

    for letter in phrase:
        for i, char in enumerate(alpha):
            # print(letter)
            if char == letter.lower():
                # print(alpha[i+shift])
                # print(letter)
                if letter.isupper():
                    res.append(alpha[i+shift].upper())    
                else: 
                    res.append(alpha[i+shift])
                
    return ''.join(res)

phrase = 'dsDFgf'
print(cipher(phrase,4))

# Runtime: 27n