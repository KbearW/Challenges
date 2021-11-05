'''
Divide and Conquer - Quick Sort

Quick sort- best runtime: O(nlog n)
worse runtime: O(n**2)
average runtime: O(nlog n)

2 methods: (In place)
1.) Lomuto's partitioning
    2 pointers, one starts at the beginning of the array, one starts at i+1 array (see below for sudo code)
2.) Hoare's partitioning
'''

'''Lomuto's'''

import random
def quicksort_lomuto(A):
    def helper(A, start, end):
        if start >= end:
            return

        pindex = random.randint(start, end)
        A[pindex], A[start] = A[start], A[pindex]
        orange = start
        for green in range(start+1, end+1):
            print(start, A[start])
            print(green, A[green])
            print(orange, A[orange])
            if A[green] < A[start]:
                orange += 1
                A[green], A[orange] = A[orange], A[green]
        A[start], A[orange] = A[orange], A[start]

        helper(A, start, orange-1)
        helper(A, orange+1, end)

    helper(A, 0, len(A)-1)
    return nums
    
nums = [4,3,9,10,2,6]
quicksort_lomuto(nums, 0, len(nums)-1)

# # Part 2: conquer
# function quicksort(A):
#     helper(A, 0, length(A)-1)
#     return A

'''Hoare's'''
# This can replace Lumoto's code from above!
                        #<--  Hoare's code -->
    # smaller = start +1 
    # bigger = end
    # while smaller < = bigger:
    #     if A[smaller] < A[start]:
    #         smarller ++
    #     else if A[bigger] > A[start]:
    #         bigger --
    #     else: // both pointer stuck
    #         swap A[smaller], A[bigger]
    #         smaller ++, bigger --
    # swap A[start], A[bigger]
                    # <-- End of Hoare's code -->

                    


def quicksort_hoares(A):
    ''' One pointer at the beginning of the list, one at the end'''

    def helper(A, start, end):
        if start >= end:
            return

        orange = start + 1
        green = end
        while orange <= green:
            if A[orange] < A[start]:
                orange += 1
            elif A[green] > A[start]:
                green -= 1
            else: #both pointers stuck
                A[orange], A[green] = A[green], A[orange]
                orange += 1
                green -= 1
        A[start], A[green] = A[green], A[start]

        helper(A, start, green -1)
        helper(A, green +1, end)

    helper(A, 0, len(A)-1)
    return A
    
nums = [4,3,9,10,2,6]
quicksort_hoares(nums)