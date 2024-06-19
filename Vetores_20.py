def main():
    vetor1 = []

    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número inteiro no intervalo [0, 50]: "))
        while numero < 0 or numero > 50:
            print("Número fora do intervalo permitido. Digite novamente.")
            numero = int(input(f"Digite o {i+1}º número inteiro no intervalo [0, 50]: "))
        vetor1.append(numero)
    vetor2 = [num for num in vetor1 if num % 2 != 0]

    print("\nPrimeiro vetor:")
    imprimir_vetor(vetor1)

    print("\nSegundo vetor (apenas números ímpares do primeiro vetor):")
    imprimir_vetor(vetor2)

def imprimir_vetor(vetor):
    for i in range(0, len(vetor), 2):
        if i + 1 < len(vetor):
            print(vetor[i], vetor[i + 1])
        else:
            print(vetor[i])

if __name__ == "__main__":
    main()