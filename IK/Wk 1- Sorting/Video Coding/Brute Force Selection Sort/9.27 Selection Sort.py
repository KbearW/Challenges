'''
Decrease and conquer- Selection Sort
based on sudo code given, code the select sort algo out
'''

def selectionsort(A):
    '''given a list of element, sort the list, A is the list of element'''
    # The result would already be in the final position. 
    # runtime: O(n**2) 
    # Space: O(1) 
    # *len(A)-1 for iteration bc the last item is already presorted per setup!
    for i in range(len(A)-1):  # 0,1,2,3
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
    '''given a list of element, sort the list and the largest elem to the left- aka, 
    smallest to the right of the list'''
    for i in range(len(array)-1):
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

print(selectionsortlargesttosmallest([6,3,2,5]))
# res should be [6,5,3,2]

# LC 922
# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3990/

# def sortArrayByParityII(nums):
        
#         This code works but time limit exceeded bc it's based on selection sort method, which is slow by itself
# Should use the 2 pointers approach

#     for i in range(len(nums)-1):
#         if i % 2 == 0 and nums[i] % 2 != 0: #index == even and num == odd
#             # find the next even num
#             # print('yes')
#             for j in range(i, len(nums)):
#                 if nums[j] % 2 == 0:
#                     # swap w the next even num
#                     nums[i], nums[j] = nums[j], nums[i]
#                     # print(nums[i], nums[j])
#         elif i % 2 != 0 and nums[i] % 2 == 0: #index == odd and num == eve
# #                     find the next odd num
#             for j in range(i, len(nums)):
#                 if nums[j] % 2 != 0:
#                     # swap w the next num
#                     nums[i], nums[j] = nums[j], nums[i]
#                     # print(nums[i], nums[j])
                
#     return nums

# # print(sortArrayByParityII([3,4]))
# # print(sortArrayByParityII([4,1,2,1]))
# print(sortArrayByParityII([4,2,5,7]))
# # res should be [4,7,2,5], [2,5,4,7], [2,7,4,5]