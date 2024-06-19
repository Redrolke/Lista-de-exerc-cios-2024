vetor = []

for i in range(10):
    valor = int(input(f"Digite o numero para a posição {i}: "))
    vetor.append(valor)
contagem_pares = 0
for valor in vetor:
    if valor % 2 == 0:
        contagem_pares += 1
print(f"O vetor possui {contagem_pares} numeros pares.")