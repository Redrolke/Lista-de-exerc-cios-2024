def encontrar_maior_valor(matriz):
    maior_valor = matriz[0][0]
    posicao = (0, 0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                posicao = (i, j)

    return posicao

def main():

    matriz = []

    for i in range(4):
        linha = []
        for j in range(4):
            valor = float(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    print("Matriz 4x4:")
    for linha in matriz:
        print(linha)
    posicao_maior_valor = encontrar_maior_valor(matriz)
    linha_maior, coluna_maior = posicao_maior_valor
    print(f"O maior valor da matriz está na posição [{linha_maior}][{coluna_maior}]")

if __name__ == "__main__":
    main()