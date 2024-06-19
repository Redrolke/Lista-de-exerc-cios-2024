def main():
    vetor = []

    for i in range(10):
        valor = int(input(f"Digite um numero {i+1}: "))
        vetor.append(valor)
    for i in range(10):
        if vetor[i] < 0:
            vetor[i] = 0
    print("\nVetor com valores negativos substituídos por 0:")
    print(vetor)

if __name__ == "__main__":
    main()