vetor = []
for i in range(10):
    valor = int(input(f"Digite um numero para a posição {i}: "))
    vetor.append(valor)
maior_valor = vetor[0]
posicao_maior = 0
for i in range(1, len(vetor)):
    if vetor[i] > maior_valor:
        maior_valor = vetor[i]
        posicao_maior = i
print("Vetor lido:")
for valor in vetor:
    print(valor, end=' ')
print()

print(f"O maior numero do vetor é: {maior_valor}")
print(f"A posição do maior numero é: {posicao_maior}")