def buscar_valor_na_matriz(matriz, valor):
    encontrado = False
    posicao = None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                encontrado = True
                posicao = (i, j)
                break
        if encontrado:
            break

    return posicao

def main():

    matriz = []

    print("Preencha a matriz 5x5:")
    for i in range(5):
        linha = []
        for j in range(5):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    valor_x = int(input("Digite o valor a ser buscado na matriz: "))
    posicao = buscar_valor_na_matriz(matriz, valor_x)
    if posicao:
        print(f"O valor {valor_x} foi encontrado na posição [{posicao[0]}][{posicao[1]}].")
    else:
        print(f"O valor {valor_x} não foi encontrado na matriz.")

if __name__ == "__main__":
    main()