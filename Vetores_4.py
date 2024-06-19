vetor = []
for i in range(8):
    valor = float(input(f"Digite o numero para a posição {i}: "))
    vetor.append(valor)
X = int(input("Digite a posição X (0 a 7): "))
Y = int(input("Digite a posição Y (0 a 7): "))

if 0 <= X < 8 and 0 <= Y < 8:
    soma = vetor[X] + vetor[Y]
    print(f"A soma dos numeros nas posições {X} e {Y} é: {soma}")
else:
    print("Posições X e Y devem estar entre 0 e 7.")