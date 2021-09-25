# https://fellowship.hackbrightacademy.com/materials/challenges/word-lengths/index.html#word-lengths    

'''give a phrase, return dict keyed by word-length, with the value of each length beingthe set of words of that length'''

# dict within dict
def word_lengths(phrase):
    lengths = {}
    words = phrase.split()

    for word in words:
        if len(word) not in lengths:
            lengths[len(word)] = set()
        lengths[len(word)].add(word)
    return lengths

phrase = "cute cats chase fuzzy rats"
print(word_lengths(phrase))