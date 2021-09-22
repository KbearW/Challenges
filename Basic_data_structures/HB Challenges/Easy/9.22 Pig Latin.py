# https://fellowship.hackbrightacademy.com/materials/challenges/pig-latin/index.html#pig-latin

# case nonsenstitive

vowels = 'aeiou'
def pig_latin(phrase):
    '''turn word into pig latin version.'''
    phrase = phrase.split()
    # print(phrase)
    res = []
    for word in phrase:
        if word[0].lower() not in vowels:
            res.append(word[1:] + word[0] + 'ay')
        else:
            res.append(word + 'yay')
            
    return ' '.join(res)

phrases = ['porcupines are cute', 'give me an apple']
for phrase in phrases:
    print(pig_latin(phrase))

# look at the input format--> in this case, it's a string... so we need to split
# case #1:
#     starts w vowels
#         ** string is immutable... need to create a new string each time...
#         move vowel to the end of the word
#         add 'ay' at the end
# caes #2:
#     not start w vowels
#         add 'yay' at the end of the word

# look at the format of the output--> it's in a string --> ' '.join(list)
# return the phrase