# function helper(A, start, end):

# # Leaf worker--> aka- base case
# if start == end:
#     return 

# # Internal node worker
# mid = (start + end)/2
# helper(A, start, mid)
# helper(A, mid+1, end)
# //merge the two sorted halves
# i = start, j = mid + 1
# aux = an empty away of size (end-start+1)
# while i < = mid and j <= end:
#     if A[i] <= A[j]:
#         aux.append(A[i])
#         i += 1
#     else: //A[i]>A[j]
#         aux.append(A[j])
#         j += 1
# //Gather phase
# while i <= mid:
#     aux.append(A[i])
#     i += 1

# while j <= end:
#     aux.append(A[j])
#     j += 1

# //copy over the elem in aux to the original list
# A[start...end] 

# Original worker:
# function mergesort(A):
    # helper(A, 0, len(A)-1)
    # return A

# Runtime: O(log n)
# Space: ?