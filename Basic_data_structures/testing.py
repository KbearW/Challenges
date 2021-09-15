import collections
def wordFrequencies(s):
    s = s.lower()
    dataset = set(s.split(' '))
    # print(dataset)
    data = {}
    for word in dataset:
        data[word] = 0
    
    for word in s.split(' '):
        # print(f'currnt word is: {word}, s is: {s}')
            data[word] += 1
    # print(data)
    return data

    # sorted_data = collections.OrderedDict(sorted(data.items()))
    # # print(type(sorted_data))
    
    # # for k,v in sorted_data.items():
    # #     # print(k,v)
    # print(sorted_data)
    # # return sorted_data.items()

    
fptr = open('empty.txt', 'w')

# result = wordFrequencies('count count count the the words')
# print(result)
# print([x for x in result.items()])

result = [('words', '1'), ('count', '3'), ('the', '2')]
# fptr.write([' '.join(x) for x in result])
fptr.write('\n'.join([' '.join(x) for x in result])) 
# fptr.write('\n')

fptr.close()  
  