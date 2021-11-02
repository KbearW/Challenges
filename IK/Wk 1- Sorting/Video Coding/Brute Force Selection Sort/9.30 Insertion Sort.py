'''
Decrease and conquer- Insertion Sort

sort the given array and perform an insertion sort'''
# sudo code
# iterate over the whole arr from 0 to n-1 position. (Last position will be already sorted automatically)
# for i in (0, n-1):
#     assign the curr position to temp
#     temp = A[i]
#     red = i-1
#     first statement is to prevent an index error when i == 0,
#     the 2nd statement is to breakout the iteration when the whole list has been sorted
#     while red >=0 and A[red] > temp:
#         Shift order by one
#         A[red + 1] = A[red]
#         move the iteration along
#         red -= 1
#         insert the ith position's value
#     A[red + 1] = temp
# return A

# For insertion sort, it's important to look at the assumption - aka the nature of the list (sorted vs sorted?)
# best case: sorted list --> one transaction --> O(n)
# worse case: list is not sorted --> O(n**2)
# Runtime: between O(n) and O(n**2)
# Average case: O(n**2)
# Space: O(n)

# Note: the while loop introduce runtime variability

def insertionsort(A):
    for i in range(len(A)):
        # must setup temp as a number rather than an index bc the array will change overtime
        temp = A[i]
        prev = i-1
        while prev >= 0 and A[prev] > temp:
            # shift the number over, it can be listed as A[i] or A[prev + 1]
            A[prev + 1] = A[prev]
            # move prev along
            prev -= 1
        # As this point, prev is in the incorrect index bc of L40, therefore, need to shift it back to the correct index --> by '+1'
        A[prev + 1] = temp
    return A

A= [4,6,7,3,8]
print(insertionsort(A))
# res should be [3,4,6,7,8]