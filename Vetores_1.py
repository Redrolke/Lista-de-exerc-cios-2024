A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]
print(f'A soma de A[0], A[1] e A[5] é: {soma}')

A[4] = 100

print("Valores do vetor A após as modificações:")
for valor in A:
    print(valor)
