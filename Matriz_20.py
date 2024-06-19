import numpy as np

matriz = np.array([
    [1.5, 2.3, 3.1, 4.7, 5.2, 6.8],
    [2.4, 3.5, 4.6, 5.7, 6.8, 7.9],
    [3.6, 4.7, 5.8, 6.9, 7.0, 8.1]
])
soma_colunas_impares = matriz[:, 0::2].sum(axis=0)
media_colunas_2_e_4 = matriz[:, [1, 3]].mean(axis=0)

matriz[:, 5] = matriz[:, 0] + matriz[:, 1]
print("Matriz modificada:")
print(matriz)
print("\nResultados:")
print(f"(a) Soma dos elementos das colunas ímpares: {soma_colunas_impares}")
print(f"(b) Média aritmética das colunas 2 e 4: {media_colunas_2_e_4}")