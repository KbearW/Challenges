# https://fellowship.hackbrightacademy.com/materials/challenges/is-palindrome/index.html#is-palindrome

# goal: retrun T/F if word is a palindorme--> spelled the same backwards and forwards
# edge: case senstitive

def is_palindorme(word):
    '''T/F if word is a palindorme'''
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
    return True

words = ['a', 'noon', 'racecar', 'porcupine', 'Racecar']
for word in words:
    print(f'for {word}, palindorme is {is_palindorme(word)}.')