Python build-in functions- Must know:

escape--> '\'

lambda --> can take any numbers of arguments but only have one expression
ie. 
x = lambda a: a+10
    print(x(5)) --> 15

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

Strings:
word= 'i love bacon!'
splitword = word.split('')
newword = ' '.join(splitword)
# Insert in list with spec position:
splitword.insert(2, "don't")

collections.Count --> will put result in dict + count
# ie- {'d':3, 'g':6}
# when using count, can use dict_name.most_common(3) to get the key of the number of values you are looking for

# word.startswith('xxx') --> will return boolean if the string starts with 'xxx'. it's not appliable for list

removes whitespace from the beginning and end of the string:
word.strip()
word.replace('love','hate')



# xx.sort() vs. sorted(xx)

xx.sort() will modify the list called in only and return None!
sorted(xx) --> will create new list--> need a new var to hold it

xx.sort(reverse = True) or xx.sort(key = sortSecond) --> will work for reverse and sort under a tuple
# ie. [(1,2),(4,1)] --> [(4,1),(1,2)]

______________________________


# dicts:
animals = {'dog':3, 'cat':6, 'panda':10, 'fish':30}
animals.keys() --> dict_keys(['dog','cat','panda','fish'])
animals.valeus() --> dict_keys([3,6,10,30])
animals.items() --> dict_items(['dog':3, 'cat':6, 'panda':10, 'fish':30])

# if you want to display it in better format- do a for loop and unpack the items:
for animal, num in animals.items():
    print(f'{animal} count is {num}')

# Remove items: pop(), popitem(), del
animals.pop('dog')
animals.popitem() <-- this will remove the last inserted item
del animals['dog']  *** Noe: del can also remove the whole array
animals.clear() <-- will empty the aaray

if you want to delete an item within dict--> use del--> del animals['dog']

if you want to avoid key error--> use .get--> animal.get('bear',0)  or animal.get('bear')

# Copy dictionaries --> can't do animals2 = animals--> this is just a reference to ansimals array 
# and changes made to animals will automatically be made to animals2 as well!!! 
animals2 = animals.copy()
or
animals2 = dict(animals)

# iterate over a string:
string1 = 'geeks for geeks'
for char in string1:
    print(char, end = ' ')
# g e e k s f o r g e e k s 

# reversed [start:end:step]
string1 = 'geeks'
for char in string1[::-1]:
    print(char, end = ' ')
# S K E E G 

for index in range(0,len(string1)):
    print(string1[index])
# G
# E
# E
# K
# S

# Reversed
for index in reversed(range(0,len(string1))):
    print(string1[index])

# s
# k
# e
# e
# g
# r
# o
# f

update an item to the dict--> use update()
thisdict =	{
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
thisdict.update({"color": "red"}) --> hisdict =	{
                                                "brand": "Ford",
                                                "model": "Mustang",
                                                "year": 1964, 
                                                "color": "red"
                                                }

