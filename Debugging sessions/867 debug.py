def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = []
    
    for i in range(len(matrix[0])):
#             create the answer range bc the input range can be [3 x2] and not n x n
        newRow = []
        for j in range(len(matrix)):
            # append the new items to a new list... more memory...
            newRow.append(matrix[j][i])
        res.append(newRow)
    
    return res
    
    # Method #2:
    # return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

# result: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# Should be: Output: [[7,4,1],[8,5,2],[9,6,3]]