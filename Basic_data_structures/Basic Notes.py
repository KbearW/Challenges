Python build-in functions- Must know:

word= 'i love bacon!'
splitword = word.split('')
newword = ' '.join(splitword)
# Insert in list with spec position:
splitword.insert(2, "don't")

collections.Count --> will put result in dict + count
# ie- {'d':3, 'g':6}
# when using count, can use dict_name.most_common(3) to get the key of the number of values you are looking for

# word.startswith('xxx') --> will return boolean if the string starts with 'xxx'. it's not appliable for list


# xx.sort() vs. sorted(xx)

xx.sort() will modify the list called in only and return None!
sorted(xx) --> will create new list--> need a new var to hold it

xx.sort(reverse = True) or xx.sort(key = sortSecond) --> will work for reverse and sort under a tuple
# ie. [(1,2),(4,1)] --> [(4,1),(1,2)]


# dicts:
animals = {'dog':3, 'cat':6, 'panda':10, 'fish':30}
animals.keys() --> dict_keys(['dog','cat','panda','fish'])
animals.valeus() --> dict_keys([3,6,10,30])
animals.items() --> dict_items(['dog':3, 'cat':6, 'panda':10, 'fish':30])

# if you want to display it in better format- do a for loop and unpack the items:
for animal, num in animals.items():
    print(f'{animal} count is {num}')

if you want to delete an item within dict--> use del--> del animals['dog']

if you want to avoid key error--> use .get--> animal.get('bear',0)