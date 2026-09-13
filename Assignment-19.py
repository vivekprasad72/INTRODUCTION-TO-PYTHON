import numpy as np

# Create a 4x4 matrix
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Transpose
transpose_A = A.T

# Find rank
rank_A = np.linalg.matrix_rank(A)

print("Original Matrix:")
print(A)

print("\nTranspose of Matrix:")
print(transpose_A)

print("\nRank of Matrix:")
print(rank_A)