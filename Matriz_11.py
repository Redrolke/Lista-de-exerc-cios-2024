import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
soma = 0
for i in range(3):
    soma += A[i][2 - i]

print("Matriz A:")
print(A)
print("\nSoma dos elementos na diagonal secundária:", soma)