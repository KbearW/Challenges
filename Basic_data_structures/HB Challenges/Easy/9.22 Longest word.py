# https://fellowship.hackbrightacademy.com/materials/challenges/longest-word/index.html#longest-word

def find_longest_word(words):
    '''takes a list of words and returns the length of the longest one'''
    # Method #1- use build-in method- max
    # len_of_word = []
    # for word in words:
    #     len_of_word.append(len(word))
    # return max(len_of_word)
    # Runtime: O(n)
    # Memory: O(n)

    # Method #2- use O(1) memory
    longest_len = len(words[0])
    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
    return longest_len

    # runtime: O(n)
    # Memory: O(1)

word_list = [["hi", "hello"],["Balloonicorn", "Hackbright"]]
for word_pair in word_list:
    print(find_longest_word(word_pair))