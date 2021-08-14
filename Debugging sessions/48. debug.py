def rotate(A):
    A.reverse()
    print(A)
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    return A

rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])