'''
Divid and Conquer - Quick Sort

Quick sort- best runtime: O(nlog n)
worse runtime: O(n**2)
average runtime: O(nlog n)

2 methods: (In place)
1.) Lomuto's partitioning
    2 pointers, one starts at the beginning of the array, one starts at i+1 array (see below for sudo code)
2.) Hoare's partitioning
'''

# Sudo Code:
# part 1: divide
# function helper(A, start, end):
#     # Leaf worker
#     if start >= end:
#         return

#     # internal node worker
#     [Lomuto's code-->]

#     small = start <-- pick a random element to avoid the worse case (skewed)-- aka sorted list 
    
#     Do this... Randomized algorithm
#     privotindex = a random int in range(start, end+1)
#     swap A[pivotindex], A[start]

#     for bigger in start +1 to end:
#         if A[bigger] < A[start]:
#             smaller ++
#             swap A[smaller], A[bigger]
#     swap A[start], A[smaller]

#     helper(A, start, smaller -1)
#     helper(A, smaller + 1, end)

# # Part 2: conquer
# function quicksort(A):
#     helper(A, 0, length(A)-1)
#     return A