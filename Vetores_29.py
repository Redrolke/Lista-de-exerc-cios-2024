def main():

    pares = []
    impares = []
    print("Digite 6 números inteiros:")
    for i in range(6):
        numero = int(input(f"Digite o número {i+1}: "))
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    soma_pares = sum(pares)

    quantidade_impares = len(impares)

    print("\nNúmeros pares digitados:")
    for num in pares:
        print(num, end=' ')

    print(f"\nSoma dos números pares digitados: {soma_pares}")

    print("\nNúmeros ímpares digitados:")
    for num in impares:
        print(num, end=' ')

    print(f"\nQuantidade de números ímpares digitados: {quantidade_impares}")

if __name__ == "__main__":
    main()