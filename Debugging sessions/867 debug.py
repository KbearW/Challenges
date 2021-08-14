def rotate(A):

    R = len(A)
    C = len(A[0])
    transpose = []
    for c in range(C):
        newRow = []
        for r in range(R):
            newRow.append(A[r][c])
        transpose.append(newRow)
    return transpose
    # return list(zip(*A))

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

# result: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# Should be: Output: [[7,4,1],[8,5,2],[9,6,3]]