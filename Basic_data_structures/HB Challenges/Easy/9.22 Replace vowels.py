# https://fellowship.hackbrightacademy.com/materials/challenges/replace-vowels/index.html#replace-vowels

'''given list of chars, return a new cpy, but w vowels replaced by *'''
# edge case: empty list --> empty list
# case none senstitive
# vowels= 'aeiou'

def replace_vowels(chars):
    '''given list of chars, return a new cpy, but w vowels replaced by *'''
    # Method #1
    # res = []
    # for char in chars:
    #     if char.lower() in 'aeiou':
    #         char = '*'
    #     res.append(char)
    # return res

    # Method #2
    return ['*' if char.lower() in 'aeiou' else char for char in chars]

chars_list = [['h', 'i'],['o', 'o', 'o'], ['z', 'z', 'z'],['A','b','C'] ,[], ['y','a','y']]
for chars in chars_list:
    print(replace_vowels(chars))