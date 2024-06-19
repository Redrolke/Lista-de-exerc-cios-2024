def main():

    vetor1 = []
    vetor2 = []
    print("Digite os 10 elementos do primeiro vetor:")
    for i in range(10):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        vetor1.append(elemento)
    print("\nDigite os 10 elementos do segundo vetor:")
    for i in range(10):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        vetor2.append(elemento)
    uniao = list(set(vetor1) | set(vetor2))

    print("\nElementos na união dos dois vetores:")
    print(uniao)
if __name__ == "__main__":
    main()