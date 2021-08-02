txt = "The best things in life are free!"
print("boolean statement--> 'in'")
print("free" in txt)

print('\n-------Slices---------')
print(f'txt[:]: {txt[:]}')
print(f'txt[5:-5]: {txt[5:-5]}')
print(f'txt[12:]: {txt[12:]}')
print(f'txt[12:50]: {txt[12:50]}')
print(f"split based on space: {txt.split(' ')}")
print(f"split based on char-t: {txt.lower().split('t')}")
print('\n------split------')
txtlist = txt.split(' ')
print(f'txtlist = {txtlist}')
print('Covert txtlist to string:--> Use build in function: "".join(list) ')
string1 = ''.join(txtlist)
print(string1)
print('\n------counter------')
#Method #1
from collections import Counter
A = Counter(string1)
print(A)
print(f'A["e"] exists {A["e"]} times.')
print(f'Dicts keys are:{A.keys()}')
print(f'Dicts values are:{A.values()}')
print(f'.items:{A.items()}')

print('\n------Dicts/ elements------')
print(sorted(A.elements()))
#print("".join(Counter("mississippi").elements()))
print(A.most_common(5))
#print(f'Most Common occurance of 6 times is: {A.most_common()}')
print('\n------------')
print(' '.join(Counter(txt).elements()))
print(f'Most freq letter is: ______?')
print(f'Least freq letter is: ______?')

# Can get intersection among diff words by:
# Counter('bella') & Counter('label') & Counter ('roller')
#--> Counter({'e':1,'l':2})

#Method #2
#import collections
#A = collections.Counter(string1)
#print(A)

A.elements

# Qs:
# How to covert list to string?
# list doesn't have attribute 'split'
#for dict, min and max functions work but it's based on the order of the key and not the value. For example: max(A) will return 't' b/c the letter 't' is the max char in the dict. For min(A), it will return '!' b/c it is before 'a'.

