# https://fellowship.hackbrightacademy.com/materials/challenges/pangram/index.html#pangram

'''return T/F if a sentence contains all the letters of english alphabet at least once.'''
# edge case: not case senstitive -->.lower()
# what about non alpha? --> use .isalpha()
# use set to remove duplicates

def is_pangram(sentence):

    return len(set(char.lower() for char in sentence if char.isalpha()))==26

sentences = ["The quick brown fox jumps over the lazy dog!", "I like cats, but not mice"]
for sentence in sentences:
    print(is_pangram(sentence))
