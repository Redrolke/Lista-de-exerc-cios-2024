import numpy as np

np.random.seed(0) 
A = np.random.randint(1, 21, size=(4, 4))
A_triang_inferior = A.copy()
for i in range(4):
    for j in range(4):
        if i < j:
            A_triang_inferior[i][j] = 0
print("Matriz Original A:")
print(A)
print("\nMatriz Triangular Inferior de A:")
print(A_triang_inferior)