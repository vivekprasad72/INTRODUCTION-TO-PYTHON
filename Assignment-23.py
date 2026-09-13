import numpy as np

# Let distance between P and Q be D
D = 110  
A = np.array([[11, -11],
              [1, 1]])

B = np.array([D, D])

v1, v2 = np.linalg.solve(A, B)

print("Velocity of first car =", v1, "km/h")
print("Velocity of second car =", v2, "km/h")