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

def multiplicar_matrizes(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

def imprimir_matriz(matriz, nome):
    print(f"\nMatriz {nome}:")
    print(matriz)

def main():
    print("Digite os elementos da Matriz A:")
    matriz_A = ler_matriz()
    print("\nDigite os elementos da Matriz B:")
    matriz_B = ler_matriz()
    if matriz_A.shape != (3, 3) or matriz_B.shape != (3, 3):
        print("Erro: As matrizes devem ter tamanho 3x3.")
        return

    matriz_C = multiplicar_matrizes(matriz_A, matriz_B)
    imprimir_matriz(matriz_A, "A")
    imprimir_matriz(matriz_B, "B")
    imprimir_matriz(matriz_C, "C = A * B")

if __name__ == "__main__":
    main()