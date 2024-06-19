def ler_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            num = int(input(f"Digite o elemento [{i}][{j}] da matriz: "))
            linha.append(num)
        matriz.append(linha)
    return matriz
def soma_colunas(matriz):
    soma_col = []
    for j in range(3):  
        soma = 0
        for i in range(3):  
            soma += matriz[i][j]
        soma_col.append(soma)
    return soma_col

def exibir_resultado(soma_col):
    print("Array unidimensional com as somas das colunas da matriz:")
    for i in range(len(soma_col)):
        print(soma_col[i], end=" ")
    print()
print("Digite os elementos da matriz 3x3:")
matriz = ler_matriz()
somas_colunas = soma_colunas(matriz)

exibir_resultado(somas_colunas)