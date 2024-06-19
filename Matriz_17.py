import numpy as np

notas = np.array([
    [7.5, 6.0, 8.5],
    [5.0, 4.5, 6.0],
    [8.0, 7.0, 7.5],
    [6.5, 7.5, 7.0],
    [4.0, 5.0, 4.0],
    [6.0, 5.5, 5.5],
    [7.0, 6.5, 6.0],
    [8.5, 9.0, 8.0],
    [5.5, 6.5, 6.0],
    [6.0, 7.0, 6.5]
])
pior_nota_prova1 = min(notas[:, 0])
pior_nota_prova2 = min(notas[:, 1])
pior_nota_prova3 = min(notas[:, 2])
count_pior_nota_prova1 = len(np.where(notas[:, 0] == pior_nota_prova1)[0])
count_pior_nota_prova2 = len(np.where(notas[:, 1] == pior_nota_prova2)[0])
count_pior_nota_prova3 = len(np.where(notas[:, 2] == pior_nota_prova3)[0])

print(f"Número de alunos com pior nota na prova 1: {count_pior_nota_prova1}")
print(f"Número de alunos com pior nota na prova 2: {count_pior_nota_prova2}")
print(f"Número de alunos com pior nota na prova 3: {count_pior_nota_prova3}")