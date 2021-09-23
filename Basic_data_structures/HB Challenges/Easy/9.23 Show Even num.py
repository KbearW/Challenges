# https://fellowship.hackbrightacademy.com/materials/challenges/show-evens/index.html#show-evens

# edge: neg--> only pos whole num
# runtime: O(n)
# space: O(1)

def show_evens(nums):
    '''return a list of the index of the evens'''
    res = []
    for i, num in enumerate(nums):
        if num % 2 == 0:
            res.append(i)
    return res

nums = [1,2,3,4,6,8]
print(show_evens(nums))