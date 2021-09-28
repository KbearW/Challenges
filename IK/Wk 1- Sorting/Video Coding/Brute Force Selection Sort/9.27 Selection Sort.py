'''based on sudo code given, code the select sort algo out'''

from abc import abstractproperty


def selectionsort(A):
    '''given a list of element, sort the list, A is the list of element'''
    # The result would already be in the final position. 
    # runtime: O(n) 
    # Space: O(n)
    for i in range(0,len(A)):  # 0,1,2,3
        # For position i
        # find the ith smallest elemt and swap wi with A[i]
        min = i
        # for selection of the elem/ counter shift
        # i+1 bc it doesn't need to loop thur the beginning of the range as it has been sorted already!
        for j in range(i+1,len(A)):  # 1,2,3,4
            # comparison
            if A[min] > A[j]:
                min = j
                # Swapping
        A[i], A[min] = A[min], A[i]
    return A


# print(selectionsort([6,3,2,5]))
# res should be [2,3,5,6]


def selectionsortlargesttosmallest(array):
    '''given a list of element, sort the list and the largest elem to the left- aka, smallest to the right of the list'''
    for i in range(len(array)):
    # start w the left most position and iterate over the array
        max = i
    #     setup max
        for j in range(i+1, len(array)):
    #     iterate over the array
            if array[max] < array[j]:
    #         if max is smaller than the current item
                max = j
    #             update max
            array[max], array[i] = array[i], array[max]
    #     swap the item
    return array

# print(selectionsortlargesttosmallest([6,3,2,5]))
# res should be [6,5,3,2]

# LC 922
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3990/

# def sortArrayByParityII(nums):
    
#     # iterate over the length of the array
#     for i in range(len(nums)):
#     #     set curr = current item
#         even = i
#         odd = i+1
#     #     iterate over the remainder array
#         for j in range(i+1, len(nums)):
#     #         if the index is even:
#             if (i+1) %2 != 0:
#                 # if num is even
#                 if nums[j] != 0:
#                     curr = j
#             nums[curr], nums[i] = nums[i], nums[curr]
#     return nums

# # print(sortArrayByParityII([3,4]))
# # print(sortArrayByParityII([4,1,2,1]))
# print(sortArrayByParityII([4,2,5,7]))
# # res should be [4,7,2,5], [2,5,4,7], [2,7,4,5]