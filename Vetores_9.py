vetor = []
while len(vetor) < 6:
    valor = int(input("Digite um numero par: "))
    if valor % 2 == 0:
        vetor.append(valor)
    else:
        print("O numero não é par. Tente novamente.")
print("Valores na ordem inversa:")
for valor in reversed(vetor):
    print(valor)