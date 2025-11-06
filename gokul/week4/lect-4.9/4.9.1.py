# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# multiply these two matrices using for loops

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


for i in range(3):         
    for j in range(3):       
        for k in range(3):   
            C[i][j] += A[i][k] * B[k][j]

# Print result
print("Matrix C (A x B):")
for row in C:
    print(row)


import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,1],[6,2,3],[4,2,1]])
C = np.dot(A, B)
print(C)
