def rotate(A):
    A.reverse()
    print(A)
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A

rotate([[1,2,3],[4,5,6],[7,8,9]])