valores = []
for i in range(10): valores.append(float(input(f"Digite um numero {i+1}: ")))

quadrados = [valor ** 2 for valor in valores]

print("numeros lidos:")
for valor in valores:
    print(valor)

print("Quadrados dos numeros:")
for quadrado in quadrados:
    print(quadrado)