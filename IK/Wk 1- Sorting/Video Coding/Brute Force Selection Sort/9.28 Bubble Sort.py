'''
Decrease and conquer- Bubble Sort

based on sudo code given, code the select sort algo out
THIS METHOD is WORSE than selection sort'''

# Bubble sort: iterate over the array, then starts from R to L to find the smallest # and keep moving it alone
# "Bubble up" in a way

# This method is very similar to Selection sort in that selection sort scan from L -> R and direct swap
# while bubble sort starts from R -> L and keep swapping the smallest item towards the L.

# *red is a pointer from R -> L
# Runtime: O(n**2)
# Space: O(n)

# sudo code:
    # for i in 0 to (n-1):
    # (note for it's only until (n-1) bc the last item is already sorted by default)
    #     for red in (n-1) down to (i+1):
    #         if A[red-1] > A[red]:
    #             swap A[red-1], A[red]
    # return A

def bubblesort(input):
    for i in range(len(input)-1):
        # print(i)
        for j in range(len(input)-1, 0, -1):
            # print(input[j-1], input[j])
            if input[j-1] > input[j]:
                input[j-1], input[j] = input[j], input[j-1]
    return input

input = [7,4,2,6,9]
print(bubblesort(input))
# res should be [2,4,6,7,9]