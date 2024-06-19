import math

def main():

    vetor = []
    print("Digite 10 números para o vetor:")
    for i in range(10):
        numero = float(input(f"Digite o número {i+1}: "))
        vetor.append(numero)
    media = sum(vetor) / len(vetor)
    soma_dos_quadrados = sum((x - media) ** 2 for x in vetor)
    desvio_padrao = math.sqrt(soma_dos_quadrados / len(vetor))
    print(f"\nMédia do vetor: {media:.2f}")
    print(f"Desvio padrão do vetor: {desvio_padrao:.2f}")

if __name__ == "__main__":
    main()