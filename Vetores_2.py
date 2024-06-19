valores = []

for i in range(6):
    valor = int(input(f'Digite o {i+1}º valor inteiro: '))
    valores.append(valor)

print("\nValores digitados:")
for valor in valores:
    print(valor)
