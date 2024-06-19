def main():

    vetor_A = []
    vetor_B = []
    print("Digite os 10 números inteiros para o vetor A:")
    for i in range(10):
        numero = int(input(f"A[{i}] = "))
        vetor_A.append(numero)
    print("\nDigite os 10 números inteiros para o vetor B:")
    for i in range(10):
        numero = int(input(f"B[{i}] = "))
        vetor_B.append(numero)
    vetor_C = [None] * 10
    for i in range(10):
        if i % 2 == 0:
            vetor_C[i] = vetor_A[i]
        else:
            vetor_C[i] = vetor_B[i]
    print("\nVetor C:")
    for i in range(10):
        print(f"C[{i}] = {vetor_C[i]}")

if __name__ == "__main__":
    main()