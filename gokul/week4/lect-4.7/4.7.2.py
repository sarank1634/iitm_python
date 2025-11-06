# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# Add these two matrices and store it in C 

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

B = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

for i in range(3):
    for j in range(3):
        c[i][j] = A[i][j] + B[i][j]

print("Matrix c (A+B):")
for row in C:
    print(row)