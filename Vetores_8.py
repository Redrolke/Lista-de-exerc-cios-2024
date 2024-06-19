vetor = []
for i in range(6):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)
print("Valores na ordem inversa:")
for valor in reversed(vetor):
    print(valor)