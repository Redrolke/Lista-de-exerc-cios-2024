import numpy as np

n = 10
A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i < j:
            A[i][j] = 2 * i + 7 * (j ** 2)
        elif i == j:
            A[i][j] = 3 * (i ** 2) + 1
        else:
            A[i][j] = 4 * (i ** 3) + 5 * (j ** 2) + 1

print("Matriz A:")
print(A)