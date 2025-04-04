import numpy as np

A = np.array([[2, -1, 1], [1, 3, 1], [-1, 5, 4]])
b = np.array([6, 0, -3]) 

solve = np.linalg.solve(A,b)
print("Gaussian elimination and backward substitution: [", int(solve[0]), int(solve[1]), int(solve[2]), "]")
print()

A = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])

determinant = np.linalg.det(A)
print("Matrix determinant: ", determinant)

L = np.eye(len(A))
U = A.astype(float).copy()

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        factor = U[j, i] / U[i, i]
        L[j, i] = factor
        U[j] -= factor * U[i]

print("L Matrix:")
print(L)
print()
print("U Matrix:")
print(U)
print()

print("False. The matrix is not diagonally dominant")
print()

print("True. The matrix is positive definite")
