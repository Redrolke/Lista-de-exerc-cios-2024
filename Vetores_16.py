def main():
    vetor = []

    for i in range(5):
        valor = float(input(f"Digite um numero {i+1}: "))
        vetor.append(valor)
    codigo = int(input("\nDigite um código (0 para sair, 1 para mostrar na ordem direta, 2 para mostrar na ordem inversa): "))
    while codigo != 0:
        if codigo == 1:
            print("\nVetor na ordem direta:")
            print(vetor)
        elif codigo == 2:
            print("\nVetor na ordem inversa:")
            print(vetor[::-1])
        else:
            print("\nCódigo inválido. Digite 0, 1 ou 2.")

        codigo = int(input("\nDigite um código (0 para sair, 1 para mostrar na ordem direta, 2 para mostrar na ordem inversa): "))

    print("\nPrograma finalizado.")

if __name__ == "__main__":
    main()