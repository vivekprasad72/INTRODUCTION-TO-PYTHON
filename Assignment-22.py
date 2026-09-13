import numpy as np
from scipy.linalg import qr, svd

# Square matrix
A = np.array([[4, 1, 2],
              [1, 3, 0],
              [2, 0, 5]])

print("Matrix A:")
print(A)

# QR decomposition
Q, R = qr(A)

print("\nQR Decomposition:")
print("Q =")
print(Q)

print("\nR =")
print(R)


# Singular Value Decomposition
U, S, Vh = svd(A)

print("\nSingular Value Decomposition:")
print("U =")
print(U)

print("\nSingular values =")
print(S)

print("\nVh =")
print(Vh)


# Least Squares
b = np.array([7, 8, 9])

x, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

print("\nLeast Squares Solution:")
print("x =")
print(x)

print("\nResiduals:")
print(residuals)

print("\nRank:")
print(rank)

print("\nSingular values:")
print(singular_values)