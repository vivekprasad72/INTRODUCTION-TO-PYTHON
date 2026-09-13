import numpy as np
from scipy.linalg import eig

# Create a 4x4 square matrix
A = np.array([
    [4, 1, 0, 0],
    [1, 4, 1, 0],
    [0, 1, 4, 1],
    [0, 0, 1, 4]
])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)

print("Matrix A:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)