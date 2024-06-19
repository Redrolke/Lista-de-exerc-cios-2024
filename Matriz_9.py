import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
soma = 0
for i in range(3):
    for j in range(3):
        if i > j:
            soma += A[i][j]

print("Matriz A:")
print(A)
print("\nSoma dos elementos abaixo da diagonal principal:", soma)