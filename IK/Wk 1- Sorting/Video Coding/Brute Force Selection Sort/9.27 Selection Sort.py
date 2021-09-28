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


print(selectionsort([6,3,2,5]))
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

print(selectionsortlargesttosmallest([6,3,2,5]))
# res should be [6,5,3,2]

    
