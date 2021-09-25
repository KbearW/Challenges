# https://fellowship.hackbrightacademy.com/materials/challenges/binary-search/index.html#binary-search

def binarysearch(num):
    '''put a binary search together'''
    assert 0 < num < 101
    num_guesses = 0

    hi = 0
    low = 101
    guess = None

    while guess != num:
        num_guesses += 1
        guess = (low + hi) // 2 + hi

        if num>guess:
            hi = guess
        elif num< guess:
            low = guess
    return num_guesses

print(binarysearch(31))