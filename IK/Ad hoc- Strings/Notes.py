# Practice:
    # prefix search problems
    # substrings problems

# Immutable

word1 = 'Interview'
s = word1
word1 = word1+' Kickstart'
print(f'word1: {word1}')
print(f's: {s}')

# word1: Interview Kickstart
# s: Interview
# Note: Because string is immuatble, once updated, it will create a new string literal
# therefore, s, the pointer, will still pointing to the old copy rather than the new word1 copy.