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

removes whitespace import builtins
from typing import Collection, Hashable
from the beginning and end of the string: 
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
animals.pop('dog') --> animals.pop(key)--> only in dicts not list
animals.popitem() <-- this will remove the last inserted item/ can only use in dicts NOT list
del animals['dog']  *** Noe: del can also remove the whole array
animals.clear() <-- will empty the aaray

for list:
list.pop(index) is okay
list.insert(index,'newitem')--> return None/ can insert tuples / can't take negative index
If you want to return the list --> use the + method


Don't use pop with iteration, the indexing will be off bc it has been popped!
ie.
l=[1,2,3,0,0,1]
for i in range(0,len(l)):
       if l[i]==0:
           l.pop(i)

# instead do this -->list comprehension!:
l = [x for x in l if x != 0]

a = [1,2,4]
b = [3]
a.append(b)
print(a)--> [1, 2, 4, [3]]

ie. a = [1,2,4]
b = a + [3] or 3 <-- note this is can be a list
print(b) --> [1, 2, 4, 3, 4]

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

# reverse
#string[::-1] [start:end:step] || return will be none bc this method modify in-place
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
# This build in can't be use for string--> reversed('hello')--> have to use--> 'hello'[::-1]
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

# bit_length() is a functino that can tell how many bits reqs to represent an integer in binary

XOR--> exlcusive or --> evalutates to 1 if only exactly 1 of the bits is set

a | b | a ^ b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0

# .append() will print and return None bc it's modifying the list in place. --Z> infinite recursion!!
# It's the same logic as .sort() print/return None
# If you would like to return the list by adding item to the list, use the + method.
ie. A= ['apple']
    print(A.append('banana')) --> None

ie. A= ['apple']
    A += ['banana']
    print(A)--> ['apple','banana']

can use extend() to combine two list into one:
A = ['A','B','C']
B = ['X','Y','Z']
A.extend(B)--> A = ['A','B','C','X','Y','Z']

# in here, bc B is a list itself, by using the append function, it will attach the whole list to the end
if used A.append(B)--> A = ['A','B','C', ['X','Y','Z']]

# intersection/ union:
lst1.intersection(lst2) is a builtin function for set (both ls1 and lst2)!

# Modulo operation:
# look for the remainder
# 25 / 7 = 3 ... 4
# 25 mod 7 = 4 --> the remainder of the prior line

# Dict/ hashtable--> O(1) complexity 
# map() create a new, empty map. returns an empty map Collection
# put(key,val) add a new k/v pair to the map. if the key is already in the map then replace the old 
# val w new val.
# get(key) given a key, return the value stored in the map/ None otherwise.
# del delete the k/v pair from the map using a statement of the form del map[key].
# len() return the number of k/v pairs stored in the map.

# Think of hashtable as an array but utilize a hash method as a mean to insert it to the right 
# position. it can have k/v pair.

# Hashtable vs. Hashmap vs. Hashset

# Hashable: k/v pair, not allow null for both key and value, no order, slow, synchronized
# Hashmap: k/v pair, allow null for both key and value, no order, fast, not synchronized
# Hashset: values only, use .add method, can use contain method--> x in hashset, unique values only
