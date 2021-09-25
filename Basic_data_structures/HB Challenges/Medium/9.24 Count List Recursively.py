# https://fellowship.hackbrightacademy.com/materials/challenges/count-recursively/index.html#count-recursively

def count_recursively(arr):
    '''count # of items in a list using recursion'''
    
    # base case:
    if not arr:
        return 0
    
    # else:
    return count_recursively(arr[1:]) +1
    

print(count_recursively([4,2,6,8,3]))