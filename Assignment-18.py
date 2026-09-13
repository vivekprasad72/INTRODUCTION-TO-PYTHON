import numpy as np
from scipy.linalg import solve

# Coefficient matrix
A = np.array([
    [2, 3],
    [4, 5]
])

# Constant matrix
B = np.array([8, 14])

# Solve the equations
x, y = solve(A, B)

print("Value of x =", x)
print("Value of y =", y)