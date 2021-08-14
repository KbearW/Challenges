def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    res = []
    
    for i in range(cols):
#             create the answer range
        newRow = []
        for j in range(rows):
            newRow.append(matrix[j][i])
        res.append(newRow)
    return res

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

# result: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# Should be: Output: [[7,4,1],[8,5,2],[9,6,3]]