# When an unbiased dice with 12 faces having the numbers from 1 to 12 is rolled, the probability of
# obtaining a prime number is . Set up a computational experiment to verify this.


# Matrix A
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix B
B = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

# Initialize result matrix C with zeros
C = [[0,0,0],[0,0,0],[0,0,0]]

# Multiply A and B
for i in range(3):
    for j in range(3):
        for k in range(3):
            C[i][j] += A[i][k] * B[k][j]

# Print result
for row in C:
    print(row)
