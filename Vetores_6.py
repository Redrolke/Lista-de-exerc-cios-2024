vetor = []
for i in range(10):
    valor = float(input(f"Digite o numero para a posição {i}: "))
    vetor.append(valor)
maior_valor = max(vetor)
menor_valor = min(vetor)

print(f"O maior valor do numero é: {maior_valor}")
print(f"O menor valor do numero é: {menor_valor}")