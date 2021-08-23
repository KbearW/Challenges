# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Method 1
        # The most pythonic solution is a simple one-liner using [::-1] to flip the matrix upside down and then zip to transpose it. It assigns the result back into A, so it's "in-place" in a sense and the OJ accepts it as such, though some people might not.
        
        # A[:] = zip(*A[::-1])
        # return A
        # Method 2
        # A.reverse()
        # print(A)
        # for i in range(len(A)):  # i = (0, 1, 2)
        #     for j in range(i):  #j = (0 or 1)  -->range(0) --> [], range(1) --> [0], range(2) --> [0,1]
        #         A[i][j], A[j][i] = A[j][i], A[i][j]
        #         print(f'i:{i}, j:{j}')
        # return A
    
    # first reverse the whole matrix, 
    # then swap each number by cooridinates- nested loop
    
#         Method #3
# Do not use [::-1] in this case since the prompt asks for in-place and [::-1] will create a new var
        A.reverse()
        print(f'L24:{A}')
        
        for r in range(3):
#             Note in here, it's not a nested for loop over range of len of array anymore. 
#             It's bc we are swapping over the diagonal--> 7,5,3, so we only need to loop thur either the top right corner or the lower left corner. If you loop thur the len of array, the whole thing will be undo. 
            for c in range(r):
                temp = A[r][c]
                A[r][c] = A[c][r]
                A[c][r] = temp

        print(A)
        return A