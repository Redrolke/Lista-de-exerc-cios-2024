import numpy as np

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

B = np.array([[16, 15, 14, 13],
              [12, 11, 10, 9],
              [8, 7, 6, 5],
              [4, 3, 2, 1]])

C = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        C[i][j] = max(A[i][j], B[i][j])

print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)
print("\nMatriz C (maiores valores de cada posição):")
print(C)