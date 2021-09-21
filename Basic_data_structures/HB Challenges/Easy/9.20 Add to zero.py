# https://fellowship.hackbrightacademy.com/materials/challenges/add-to-zero/index.html#add-to-zero


# Goal: return True if any two nums in list sum to 0.and

# def a function
# condition: 
# if 0 in list:
#     True
# iterate over the list and see if the -num in the list:
#     return True 

def add_to_zero(nums):
    '''given list of ints, return True if any two nums sum to 0.'''
    nums = set(nums)  #<-- by using set(), run time will be O(1)
    for num in nums:
        if -num in nums:
            return True
    return False

nums = [0,1,2]
print(add_to_zero(nums))