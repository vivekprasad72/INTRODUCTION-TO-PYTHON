import numpy as np

# Define two 3x3 matrices
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 10]
])

B = np.array([
    [2, 1, 3],
    [4, 5, 6],
    [7, 2, 8]
])

# 1. Inverse of matrix A
inverse_A = np.linalg.inv(A)
print("Inverse of A:")
print(inverse_A)

# 2. Determinant of matrix B
det_B = np.linalg.det(B)
print("\nDeterminant of B:")
print(det_B)

# 3. A.transpose of A
A_bar = np.transpose(A)
results = np.dot(A, A_bar)

print("\nA . A-bar:")
print(results)
