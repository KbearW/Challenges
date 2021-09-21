# https://fellowship.hackbrightacademy.com/materials/challenges/has-more-vowels/index.html#has-more-vowels

# Goal: return true if contains more vowels than non-vowels, else return False
# will have upper and lower cases

# def function
# vowels = 'aeiou'
# count = 0
# iterate over input
# if in vowels, count +1
# if len(input) - count > count:
# return False
# else return True

def has_more_vowels(input):
    '''answer the Q: contains more vowels han non-vowels?'''
    # can use set here...> {'a','e','i','o','u'}
    vowels = 'aeiou'
    count = 0
    for char in input.lower():
        if char in vowels:
            count += 1
    if len(input) - count >= count:
        return False
    else:
        return True


input = 'yay'
print(has_more_vowels(input))