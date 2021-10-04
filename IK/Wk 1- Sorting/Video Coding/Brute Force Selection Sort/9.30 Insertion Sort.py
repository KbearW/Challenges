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
    for i in range(0,len(A)-1):
        temp = A[i]
        red = i-1
        while red >= 0 and A[red] > temp:
            A[red + 1] = A[red]
            red -= 1
        A[red + 1] = temp
    return A

A= [4,6,7,3,8]
print(insertionsort(A))
# res should be [3,4,6,7,8]