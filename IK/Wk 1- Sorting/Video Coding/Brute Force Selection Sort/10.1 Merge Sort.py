'''
Divide and Conquer - Merge Sort
Divide/ Solve/ Combine

Merge Sort:
Runtime: O(n log n)
Space: O(n) 
'''
def mergesort(A):
    
    def helper(A, start, end):
        # Base case
        if start == end:
            return 

        # internal node
        mid = int((start+end)/2)
        helper(A, start, mid)
        helper(A, mid+1, end)
        i = start
        j = mid +1
        res = []
        # print(mid, i, j)

        while i <= mid and j <= end:
            if A[i] <= A[j]:
                res.append(A[i])
                i += 1
            else:
                # A[i] > A[j]:
                res.append(A[j])
                j += 1

        # Gather phrase
        while i <= mid:
            res.append(A[i])
            i += 1
        while j <= end:
            res.append(A[j])
            j += 1
            
        print(res)

        # copy the elements from the aux array back into the original subarray
        A[start:end+1] = res

    helper(A, 0, len(A)-1)
    return A
    
# Runtime: O(n log n)
# Space: req extra memory - O(n)

A = [4,5,2,5,7,8]
print(mergesort(A))