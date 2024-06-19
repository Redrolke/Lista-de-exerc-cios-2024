def main():

    v = []
    print("Digite 10 números inteiros para o vetor v:")
    for i in range(10):
        numero = int(input(f"Digite o número {i+1}: "))
        v.append(numero)
    v1 = []
    v2 = []
    for numero in v:
        if numero % 2 == 0:
            v2.append(numero)
        else:
            v1.append(numero)
    print("\nElementos utilizados de v1 (ímpares):")
    for num in v1:
        print(num, end=' ')

    print("\n\nElementos utilizados de v2 (pares):")
    for num in v2:
        print(num, end=' ')

if __name__ == "__main__":
    main()