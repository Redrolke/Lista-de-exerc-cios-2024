def main():
    valores = []

    for i in range(5):
        valor = float(input(f"Digite o {i+1}º numero: "))
        valores.append(valor)
    maior = valores[0]
    menor = valores[0]
    posicao_maior = 0
    posicao_menor = 0

    for i in range(1, 5):
        if valores[i] > maior:
            maior = valores[i]
            posicao_maior = i
        if valores[i] < menor:
            menor = valores[i]
            posicao_menor = i
    print(f"\nPosição do maior numero ({maior}): {posicao_maior + 1}")
    print(f"Posição do menor numero ({menor}): {posicao_menor + 1}")

if __name__ == "__main__":
    main()