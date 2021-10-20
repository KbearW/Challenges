'''
Divide and Conquer - Merge Sort
Divide/ Solve/ Combine

Merge Sort:
Runtime: O(n log n)
Space: O() 
'''
# function helper(A, start, end):
def helper(A, start, end):
# # Leaf worker--> aka- base case
# if start == end:
#     return 

# This line caused: RecursionError: maximum recursion depth exceeded 
    if start == end: 
        return
 
# # Internal node worker  
# mid = (start + end)/2
    mid = (start + (end - start))/2
# helper(A, start, mid)
# helper(A, mid+1, end)
    helper(A, start, mid)
    helper(A, mid+1, end)
# //merge the two sorted halves
# i = start, j = mid + 1
    i, j = start, mid +1
# aux = an empty away of size (end-start+1)
    res = []
# while i < = mid and j <= end:
    while i <= mid and j <= end:
#     if A[i] <= A[j]:
        if A[i] <= A[j]:
#         aux.append(A[i])
            res.append(A[i])
#         i += 1
            i += 1
#     else: //A[i]>A[j]
        else:
#         aux.append(A[j])
            res.append(A[j])
#         j += 1
            j += 1
# //Gather phase
# while i <= mid:
    while i <= mid:
#     aux.append(A[i])
        res.append(A[i])
#     i += 1
        i += 1

# while j <= end:
    while j <= end:
#     aux.append(A[j])
        res.append(A[j])
#     j += 1
        j +=1

# //copy over the elem in aux to the original list
# A[start...end] 
    A = res

# Original worker:
# function mergesort(A):
    # helper(A, 0, len(A)-1)
    # return A

def mergesort(A):
    helper(A, 0, len(A)-1)
    return A
# Runtime: O(n log n)
# Space: req extra memory - O(n)

A = [4,5,2,5,7,8]
print(mergesort(A))