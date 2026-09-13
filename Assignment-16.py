import numpy as np

# Coefficient matrix
A = np.array([
    [3, -5],
    [4, -2]
])

# Constant matrix
B = np.array([10, 7])

# Solve the equations
X = np.linalg.solve(A, B)

print("Value of X =", X[0])
print("Value of Y =", X[1])