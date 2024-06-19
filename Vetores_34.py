def main():
    vetor = []

    print("Digite 10 números diferentes:")
    for i in range(10):
        while True:
            numero = int(input(f"Digite o número {i+1}: "))
            if numero not in vetor:
                vetor.append(numero)
                break
            else:
                print("Número já foi digitado. Digite outro número.")
    print("\nVetor final digitado:")
    print(vetor)
if __name__ == "__main__":
    main()