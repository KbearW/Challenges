# https://fellowship.hackbrightacademy.com/materials/challenges/word-count/index.html#word-count



# edge: case senstitive

# split, collection.counter or dict
# iterate over the dict and print( each k/v pair)

def word_count(phrase):
    '''given a phrase, print the word count in asc order'''
    words = phrase.split()
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    res = [ (k, v) for k,v in sorted(counter.items())]
    res.sort()

    for k, v in res:
        print((k, v))

phrases = ["berry cherry cherry cherry berry apple", "hey hi hello", "hi Hi hi"]
for phrase in phrases:
    word_count(phrase)