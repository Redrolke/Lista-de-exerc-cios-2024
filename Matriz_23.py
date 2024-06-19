import numpy as np

def ler_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = float(input(f"Digite o valor da posição [{i+1}][{j+1}] da matriz: "))
            linha.append(valor)
        matriz.append(linha)
    return np.array(matriz)

def calcular_quadrado_matriz(matriz):
    return np.dot(matriz, matriz)

def imprimir_matriz(matriz, nome):
    print(f"\nMatriz {nome}:")
    print(matriz)

def main():
    print("Digite os elementos da Matriz A:")
    matriz_A = ler_matriz()
    if matriz_A.shape != (3, 3):
        print("Erro: A matriz deve ter tamanho 3x3.")
        return

    matriz_B = calcular_quadrado_matriz(matriz_A)
    imprimir_matriz(matriz_A, "A")
    imprimir_matriz(matriz_B, "B = A^2")

if __name__ == "__main__":
    main()