# https://fellowship.hackbrightacademy.com/materials/challenges/find-range/index.html#find-range

# Goal: find the smallest and largest num
# edge case: 
# when the list is empty, return none for smallest and largest
# when the list has one int, return the same int for smallest and largest

# def function that takes in a list
# setup min and max as None
# if len(input) equals to 1
#     max, min = val within list

# iterate over the input list
# set min and max equal to init num
# if next elem smaller than min, set min as new elem
# if next elem larger than max, set max as new elem
# return (min, max)

def find_range(nums):
    # Method #1 Without built in method
    # if len(nums) < 1:
    #     min, max = None, None
    # else:
    #     max = min = nums[0]
    #     for num in nums:
    #         if max < num:
    #             max = num
    #         if min > num:
    #             min = num
    # return (min, max)

    # Method #2 use built in method
    min_val = min(nums)
    max_val = max(nums)
    return (min_val,max_val)

nums = [43, 3, 44, 20, 2, 1, 100]
print(find_range(nums))