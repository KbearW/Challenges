# https://fellowship.hackbrightacademy.com/materials/challenges/anagram-of-palindrome/index.html#anagram-of-palindrome

'''T/F if it's anagram of a palindrome'''

# edge case: only alph
# case insenstitive
# 'a'--> true
# 'ab' --> F
# 'arceace' --> T
# 'arceaceb' --> F

def is_anagram_of_palindrome(word):
    length = len(word)
    count = {}
    for char in word:
      
    seen_an_odd = False

    for v in count.values():
        if v % 2 != 0:
            if seen_an_odd:
                return False
        seen_an_odd = True
    return True


words = ['a','ab','aab','arceace','arceaceb']
for word in words:
    print(is_anagram_of_palindrome(word))