def main():
    vetor = []

    for i in range(10):
        valor = int(input(f"Digite um numero {i+1}: "))
        vetor.append(valor)

    x = int(input("\nDigite o número x para encontrar os múltiplos: "))
    print(f"\nMúltiplos de {x} no vetor:")
    encontrados = False
    for valor in vetor:
        if valor % x == 0:
            print(valor)
            encontrados = True

    if not encontrados:
        print(f"Não foram encontrados múltiplos de {x} no vetor.")

if __name__ == "__main__":
    main()