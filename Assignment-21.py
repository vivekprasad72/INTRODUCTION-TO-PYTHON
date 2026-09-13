import numpy as np
from scipy.linalg import lu

# Create a 4x4 matrix
A = np.array([
    [4, 1, 0, 0],
    [1, 4, 1, 0],
    [0, 1, 4, 1],
    [0, 0, 1, 4]
])

# Find P, L, U
P, L, U = lu(A)

print("Matrix A:")
print(A)

print("\nP Matrix:")
print(P)

print("\nL Matrix:")
print(L)

print("\nU Matrix:")
print(U)