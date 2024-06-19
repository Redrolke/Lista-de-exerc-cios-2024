def main():

    vetor_A = []
    vetor_B = []
    print("Digite os 5 números reais para o vetor A:")
    for i in range(5):
        numero = float(input(f"A[{i}] = "))
        vetor_A.append(numero)
    print("\nDigite os 5 números reais para o vetor B:")
    for i in range(5):
        numero = float(input(f"B[{i}] = "))
        vetor_B.append(numero)
    produto_escalar = 0
    for i in range(5):
        produto_escalar += vetor_A[i] * vetor_B[i]
    print("\nVetor A:")
    for i in range(5):
        print(f"A[{i}] = {vetor_A[i]}")
    print("\nVetor B:")
    for i in range(5):
        print(f"B[{i}] = {vetor_B[i]}")

    print(f"\nProduto Escalar: {produto_escalar}")

if __name__ == "__main__":
    main()