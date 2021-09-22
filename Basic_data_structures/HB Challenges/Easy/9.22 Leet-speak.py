# https://fellowship.hackbrightacademy.com/materials/challenges/leet-speak/index.html#leet-speak

# setup dict 

# runtime: O(n**2) bc string is immutable and each time will create a new string

pair = {'a':'@', 
        'o':'0',
        'e':'3',
        'l':'1',
        's':'5',
        't':'7'}
        
def translate_leet(word):
    '''translate word by replacing special chars'''

    res = ''
    for char in word:
        res += pair.get(char.lower(), char)
        
    return res


words = ['Hi Balloonicorn', "Hackbright is the Shizzle"]
for word in words:
    print(translate_leet(word))