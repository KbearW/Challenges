# https://fellowship.hackbrightacademy.com/materials/challenges/remove-duplicates/index.html#remove-duplicates

# edge case: 
#     when input is None,
#     when input are all the same #
#     when input repeat itself

def deduped(input):
    '''Goal: given a list, returns a new list of those order but remove duplicates'''
    # Method #1- this wouldn't work properly bc it's sorted and we want to retain the init order
    # return [x for x in set(sorted(input))]

    # Method #2- this wouldn't work either bc set doesn't retain the order
    # return [x for x in set(sorted(input))]

    # Method #3
    seen = set()
    res = []
    for num in input:
        if num not in seen:
            res.append(num)
            seen.add(num)
    return res

inputs = [[1,1,1], [1, 2, 1, 1, 3], [1,2,3],[], [3,4,2,1,1]]
for input in inputs:
    print(deduped(input))