# https://fellowship.hackbrightacademy.com/materials/challenges/has-unique-chars/index.html#has-unique-chars

# Goal: if contains only unique char, return True, else False. 
# edge: case senstitive, if the char is empty, return True

def has_unique_chars(word):
    # Method #1
    # char_dict = {}
    # for char in word:
    #     if char in char_dict.keys():
    #         return False
    #     else:
    #         char_dict[char] = 1
    # return True
    
    # Method #2
    unique_char = set(word)
    return len(word) == len(unique_char)

word = 'Bob'
print(has_unique_chars(word))